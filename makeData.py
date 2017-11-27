import sys
import random

print('Loading Aminer-Paper.txt')
with open('Aminer-Paper.txt','r') as f:
	lines = list(f.readlines())
print('Complete!')
print('Loading Aminer-Author.txt')
with open('AMiner-Author.txt','r') as f:
        Alines = list(f.readlines())
print('Complete!')


print()
print('Creating raw author dictionary at No.')
#Author dictionary raw data from Aminer-Paper.txt
Author_University_Raw = {}
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
            affiliation = Alines[i+2][3:]
            if len(affiliation)>3:
                j = 0
                while(True):
                    try:
                        x = Author_University_Raw[(key,j)]
                        j = j + 1
                    except KeyError:
                        Author_University_Raw[(key,j)] = affiliation 
                        if j == 0:
                            count = count + 1
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
    print('|------- Name:' + str(list(Author_University_Raw.keys())[x]) +' Affiliations:'+ str(list(Author_University_Raw.values())[x]))    
print()
 
#Loading author information from Aminer-Paper.txt, pairing with chronical information
valid = 0
inValid = 0
i = 0
while(i+3 < len(lines)):
    key = ''
    currU = ''
    
    if len(lines[i])<6:
        i = i + 1
    elif lines[i][1] == 'i' and lines[i][2] == 'n' and lines[i][3] == 'd' and lines[i][4] == 'e' and lines[i][5] == 'x':
        key = lines[i+2][3:]
        currU = lines[i+3][3:]
        i = i + 5
        # if ; in names, which means there are 2 more authors in this paper    
        if ';' in key:
            authors = key.split(';')
            affiliations = currU.split(';')
        # only one author        
        else:
            authors = [key]
            affiliations = [currU]
        authors[-1] = authors[-1][:-1]
        affiliations[-1] = affiliations[-1][:-1]
        for ind in range(0,len(authors)):
            if len(authors) != len(affiliations):
                break
            j = 0
            while(True):
                try:
                    if affiliations[ind] in Author_University_Raw[(authors[ind],j)]:
                        valid = valid + 1
                        break
                    else:    
                        j = j + 1
                except KeyError:
                    inValid = inValid + 1
                    break
    else:
        i = i + 1 
    if i%2500000 == 0:
        print(i)
print(i)

print('Total amount valid authors in paper is:' + str(valid))
print('Total amount invalid authors in paper is:' + str(inValid))
