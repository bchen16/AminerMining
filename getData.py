import sys




with open('AMiner-Author.txt','r') as f:
	lines = list(f.readlines())
d = {}
key = ['univ','inc','corp','scho','lab','service','research','inst']
for i in lines:
	if len(i) > 10:
		if i[1] == 'a':
			raw = i[3:]
			raw = raw.split(';')
			for j in raw:
				temp = j.split(',')
				for k in range(0,len(temp)):
					t = ''
					for l in key:
						if l in temp[k].lower():
							t = t + ',' + temp[k]
						else:
							d[t] = temp[k+1:]

print(len(d))
#for i,j in d.items():
#	print(i)
#	print(j)
	



		
