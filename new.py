import sys

with open('Aminer-Paper.txt','r') as f:
	lines = list(f.readlines())

Author_Univ_Year={}
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
    #multi_author_del.append(author_key)
    multi_author=author_key.split(';')
    univ_key=list(Author_Univ_Year[author_key].keys())[0]
    multi_univ=str(univ_key).split(';')
    year=Author_Univ_Year[author_key][univ_key]
    #year=1
    for i,j in zip(multi_author,multi_univ):
        if i in Author_Univ_Year:
            if j in Author_Univ_Year[i]:
                        #if year not in Author_Univ_Year[i][j]:
                Author_Univ_Year[i][j].append(year)
            else:
        
                Author_Univ_Year[i].setdefault(j,[])
                Author_Univ_Year[i][j].append(year)
        else:
           
            Author_Univ_Year.setdefault(i,{})
            Author_Univ_Year[i].setdefault(j,[])
            Author_Univ_Year[i][j].append(year)
for author_key in multi_author_del:
	Author_Univ_Year.pop(author_key,None)
