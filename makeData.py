import sys
import random
import json
import numpy as np

# judge whether to keep interest
def judge_interest(interest, interests_list):
    for i in interests_list:
        if i in interest:
            return True
    return False

#load data from interest, address dictionary (raw address -> affiliation name), clean affiliation dictionary (affiliation name -> address)
def load_clean_address(dirty_addr,addr_dict,clean_affi_dict,country_dict):
    try:
        temp_json = json.loads(clean_affi_dict[addr_dict[dirty_addr]])
    except KeyError:
        return -1

    #No result
    if len(temp_json['results']) < 1:
        return -1 # Fail
    else:
        format_addr = temp_json['results'][0]['formatted_address'].split(',')
        if len(format_addr) < 2:
            return format_addr[0].strip('01234567890 '),'',(temp_json['results'][0]['geometry']['location']['lat'],temp_json['results'][0]['geometry']['location']['lng']) 

        if format_addr[0][0] == ' ':
            format_addr[0] = format_addri[0][1:]
        if format_addr[-1][0] == ' ':
            format_addr[-1] = format_addr[-1][1:]
        format_addr[-1] = format_addr[-1].strip('0123456789 ')

        # deal with wierd contries
        wierd = False
        wierd_cou_names = ['iran','egypt','saudi arabia','taiwan']
        for c_name in wierd_cou_names:
            if c_name in ''.join(format_addr):
                wierd = True
                temp_country = c_name
                break

        # Normal countries
        if not wierd:
            try:
                country_dict[format_addr[-1].lower()]
                # country and city information of current transaction
                temp_country = format_addr[-1]
                temp_city = format_addr[-2].strip('0123456789 ')
                temp_loc = temp_json['results'][0]['geometry']['location']['lat'],temp_json['results'][0]['geometry']['location']['lng']
            except KeyError: 
                # Some counties has reversed address system
                try:
                    country_dict[format_addr[0].lower()]
                    # country and city information of current transaction (reversed address system)
                    temp_country = format_addr[0]
                    temp_city = format_addr[1]
                except KeyError:
                    # Not in country dictionary
                    return -1
        else:
            # wierd contiries
            temp_city = format_addr[-2]

        # geometric information of current transaction
        temp_loc = temp_json['results'][0]['geometry']['location']['lat'],temp_json['results'][0]['geometry']['location']['lng']

        return temp_country, temp_city, temp_loc

#Load dictionaries
addr_dict = np.load('dict_rawAddr_cleanAffiName.npy').item()
clean_affi_dict = np.load('dict_cleanAffiName_Json.npy').item()
country_dict = np.load('dict_country.npy').item()

print('Loading Aminer-Paper.txt')
with open('Aminer-Paper.txt','r') as f:
	lines = list(f.readlines())
print('Complete!')
print('Loading Aminer-Author.txt')
with open('AMiner-Author.txt','r') as f:
        Alines = list(f.readlines())
print('Complete!')
with open('interest','r') as f:
        interests_list = list(f.readlines())

iTemp = interests_list
interests_list = []
for i in iTemp:
    interests_list.append(i[0:-1])

print()
print('Creating raw author dictionary at No.')
#Author dictionary raw data from Aminer-Author.txt
Author_University_Raw = {}
#Author dictionary, author -> Field of interest from a valid interest list('interest.txt')
Author_Interests_Raw = {}
#Usable Author dictionary, with author name/affiliation-year information
    #key:('string' name.'int' times appeared)
    #affiliation:[('string' university raw name,'int' year)]
Author_Univ_Year={}



#Loading author information from Aminer-Author.txt, omitting those without affiliation
i = 0
count = 0
while(i < len(Alines)):
    key = ''
    affiliation  = ''
    if  len(Alines[i]) > 6:
        if Alines[i][1] == 'i' and Alines[i][2] == 'n' and Alines[i][3] == 'd' and Alines[i][4] == 'e' and Alines[i][5] == 'x':
            key = Alines[i+1][3:]
            key = key[:-1]
            affiliation = Alines[i+2][3:-1]
            raw_interest = Alines[i+8][3:]
            raw_interest = raw_interest.lower()
            interests = raw_interest.split(';')
            
            delete_index = []
            for idd in range(0,len(interests)):
                if not judge_interest(interests[idd], interests_list):
                    delete_index.append(idd)

            for idd in range(0,len(delete_index)):
                del interests[delete_index[idd] - idd]
                
            if len(affiliation)>3:
                j = 0
                while(True):
                    # Adding affiliations
                    try:
                        x = Author_University_Raw[(key,j)]
                        j = j + 1
                    except KeyError:
                        Author_University_Raw[(key,j)] = affiliation 
                        if j == 0:
                            count = count + 1
                        break
                while(True):
                    # Adding interests
                    try:
                        x = Author_Interests_Raw[(key,j)]
                        j = j + 1
                    except KeyError:
                        Author_Interests_Raw[(key,j)] = interests 
                        break
            i = i + 9       
        else:
            i = i + 1
    else:
        i = i + 1
    if i%2500000 == 0:
        print(len(Author_University_Raw))

print('Total author loaded with affiliation(s):' + str(count))
print('Printing 10 random authors in raw author data:')
for i in range(0,10):
    x = random.randint(0,834938)
    print('|------- Name:' + str(list(Author_University_Raw.keys())[x]) +'\n'+ str(list(Author_University_Raw.values())[x]))    
print()

#Loading author information from Aminer-Paper.txt, pairing with chronical information
valid = 0
inValid = 0
i = 0

while(i+3 < len(lines)):
    key = ''
    currU = ''
    #Read from the lines as blocks, starting from '#index'(decrease running time)
    #Abort if length < 6 (cannot be data)    
    if len(lines[i])<6:
        i = i + 1
    #Keep going if the line is index
    elif lines[i][1] == 'i' and lines[i][2] == 'n' and lines[i][3] == 'd' and lines[i][4] == 'e' and lines[i][5] == 'x':
        #key: author name
        #currU: affiliations
        key = lines[i+2][3:]
        currU = lines[i+3][3:]
        # if ; in names, which means there are 2 more authors in this paper    
        if ';' in key:
            authors = key.split(';')
            affiliations = currU.split(';')
        # only one author        
        else:
            authors = [key]
            affiliations = [currU]
        # elimintate '\n'
        authors[-1] = authors[-1][:-1]
        affiliations[-1] = affiliations[-1][:-1]
        #Add infromation to dictionary
        for ind in range(0,len(authors)):
            if len(authors) != len(affiliations):
                break
            j = 0
            while(True):
                yr = lines[i+4][3:len(lines[i+4])-1]
                try:
                    #Test if the affiliation read in paper exist in Author_Raw dictionary
                    if affiliations[ind] in Author_University_Raw[(authors[ind],j)]:
                        valid = valid + 1
                        try:
                            
                            #if author exists, add to end
                            clean_affi = load_clean_address(Author_University_Raw[(authors[ind],j)],addr_dict,clean_affi_dict,country_dict)
                            if clean_affi == -1:
                                break 
                            Author_Univ_Year[(authors[ind],j)][0].append((addr_dict[Author_University_Raw[(authors[ind],j)]],clean_affi,yr))
                        except KeyError:
                            clean_affi = load_clean_address(Author_University_Raw[(authors[ind],j)],addr_dict,clean_affi_dict,country_dict)
                            if clean_affi == -1:
                                break    
                            #if author does not exist, creat
                            interest_clean = Author_Interests_Raw[(authors[ind],j)]
                            Author_Univ_Year[(authors[ind],j)] = [[(addr_dict[Author_University_Raw[(authors[ind],j)]],clean_affi,yr)],[interest_clean]]
                        break
                    else:    
                        j = j + 1
                # The author does not even exist
                except KeyError:
                    inValid = inValid + 1
                    break
        i = i + 5
    else:
        i = i + 1 
    if i%2500000 == 0:
        print(i)
print(i)

print('Total amount valid authors in paper is:' + str(len(Author_Univ_Year)))
print('Total amount invalid authors in paper is:' + str(inValid))

print('Printing 10 random authors in corrected author data:')
for i in range(0,100):
    x = random.randint(0,len(Author_Univ_Year)-1) 
    print('|------- Name:' + str(list(Author_Univ_Year.keys())[x]) +'\n'+ str(list(Author_Univ_Year.values())[x]))
print()
np.save('final_warehouse.npy', Author_Univ_Year) 

