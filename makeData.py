import sys

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
while(i < len(Alines)):
    key = ''
    affiliation  = ''
    if  len(Alines[i]) > 6:
        if Alines[i][1] == 'i' and Alines[i][2] == 'n' and Alines[i][3] == 'd' and Alines[i][4] == 'e' and Alines[i][5] == 'x':
            key = Alines[i+1][3:]
            affiliation = Alines[i+2][3:]
            if len(affiliation)>3:
                Author_University_Raw[key] = affiliation
            i = i + 9       
        else:
            i = i + 1
    else:
        i = i + 1
    if i%2500000 == 0:
        print(len(Author_University_Raw))

print('Total author loaded with affiliation(s):' + str(len(Author_University_Raw)))

#Loading author information from Aminer-Paper.txt, pairing with chronical information
i = 0
while(i+3 < len(lines)):
    key = ''
    currU = ''
    affiliation = []
    if len(lines[i])<6:
        i = i + 1
    elif lines[i][1] == 'i' and lines[i][2] == 'n' and lines[i][3] == 'd' and lines[i][4] == 'e' and lines[i][5] == 'x':
        key = lines[i+2][3:]
        currU = lines[i+3][3:]
        i = i + 5
    else:
        i = i + 1 
    if i%2500000 == 0:
        print(i)
print(i)

