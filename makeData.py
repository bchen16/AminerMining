import sys

print('Loading Aminer-Paper.txt')
with open('Aminer-Paper.txt','r') as f:
	lines = list(f.readlines())
print('Complete!')
print('Loading Aminer-Author.txt')
with open('AMiner-Author.txt','r') as f:
        Alines = list(f.readlines())
print('Complete!')

#Author dictionary raw data from Aminer-Paper.txt
Author_RawUniversity = {}
#Usable Author dictionary, with author name/affiliation-year information
Author_Univ_Year={}

#Loading author information from Aminer-Author.txt, omitting those without affiliation
i = 0
while(i < len(Alines)):
    key = ''
    affiliation  = ''
    if  len(Alines[i]) > 6:
        if Alines[i][1] == 'i' and Alines[i][2] == 'n' and Alines[i][3] == 'd' and Alines[i][4] == 'e' and Alines[i][5] == 'x':
            key = Alines[i+1][3:]
            affiliation = Alines[i+2][3:]
            if len(affiliation)>8:
                Author_RawUniversity[key] = affiliation
            i = i + 9       
        else:
            i = i + 1
    else:
        i = i + 1
    if i%1000000 == 0:
        print(len(Author_RawUniversity))

print('Total author loaded with affiliation(s):' + str(len(Author_RawUniversity)))


#Loading author information from Aminer-Paper.txt, pairing with chronical information
multi_author=[]
multi_univ=[]
multi_author_del=[]

for i in range(len(lines)):
    if len(lines[i]) > 4:
        if lines[i][1] == '@' and lines[i+1][3]!='-':
            author_key = lines[i][3:-1]
            univ_key=lines[i+1][3:-1]
            
            if ';' in author_key:
                multi_author_del.append(author_key)
            
            Author_Univ_Year.setdefault(author_key,{}) 
            if univ_key in Author_Univ_Year[author_key]:
                Author_Univ_Year[author_key][univ_key].append(lines[i+2][3:-1])
            else:
                Author_Univ_Year[author_key].setdefault(univ_key,[])
                Author_Univ_Year[author_key][univ_key].append(lines[i+2][3:-1])
                
for  author_key in multi_author_del:
    multi_author=author_key.split(';')
    univ_key=list(Author_Univ_Year[author_key].keys())[0]
    multi_univ=str(univ_key).split(';')
    year=Author_Univ_Year[author_key][univ_key]
    for i,j in zip(multi_author,multi_univ):
        if i in Author_Univ_Year:
            if j in Author_Univ_Year[i]:
                Author_Univ_Year[i][j].append(year)
            else:
        
                Author_Univ_Year[i].setdefault(j,[])
                Author_Univ_Year[i][j].append(year)
        else:
           
            Author_Univ_Year.setdefault(i,{})
            Author_Univ_Year[i].setdefault(j,[])
            Author_Univ_Year[i][j].append(year)

for  author_key in multi_author_del:
        Author_Univ_Year.pop(author_key,None)
    

                
