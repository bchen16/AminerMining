import sys

with open('AMiner-Author.txt','r') as f:
	lines = list(f.readlines())

University = []

for i in lines:
	if len(i) > 10:
		if i[1] == 'a':
			raw = i[3:]
			raw = raw.split(',')
			for j in raw:
				University.append(j)
for i in range(0,100):
    print(University[i])

f1 = open('affiliations.txt','w')
for i in University:
	f1.write("%s\n" % i)
