import sys

with open('Aminer-Paper.txt','r') as f:
	lines = list(f.readlines())

Author_Univ_Year={}


#Author_Univ_Year.setdefault(author_key,[])
for i in range(50):
    if len(lines[i]) > 4:
        if lines[i][1] == '@':
            author_key = lines[i][3:-1]
            univ_key=lines[i+1][3:-1]
            
            #Univ_Year.setdefault(univ_key,[])
            #Univ_Year={}
            #Univ_Year[univ_key].append(lines[i+2][3:-1])
            
            Author_Univ_Year.setdefault(author_key,{})
            if univ_key in Author_Univ_Year[author_key]:
                Author_Univ_Year[author_key][univ_key].append(lines[i+2][3:-1])
            else:
                
                Author_Univ_Year[author_key].setdefault(univ_key,[])
                Author_Univ_Year[author_key][univ_key].append(lines[i+2][3:-1])

Author_Univ_Year
