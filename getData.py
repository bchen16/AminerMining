import sys

with open('AMiner-Author.txt','r') as f:
	lines = list(f.readlines())
d = {}
count = 0
ccount = 0
key = ['univ','institude']
with open('interest') as fa:
    key1 = list(fa.readlines())

for i in range(0,len(key1)):
    if key1[i] == '\n':
        del key1[i]
    else:
        key1[i] = key1[i][0:-1]


print(key1)
print(len(lines))
for i in range(0,len(lines)):
	if len(lines[i]) > 10:
		if lines[i][1] == 'a':
                        tempInt = lines[i+6][3:]
                        ti = tempInt.split(';')
                        tttt = False
                        for ip in ti:
                            for kw in key1:
                                if kw in ip:
                                    tttt = True
                        if not tttt:
                            continue
                        raw = lines[i][3:]
                        raw = raw.split(';')
                        for j in raw:
                            t = j.split(',')
                            x = 'a' 
                            for k in range(0,len(t)):
                                for l in key:
                                    if l in t[k].lower():
                                        x = ''.join(t[k])
                                        break
                                if x!='a':
                                    break
                            if len(x)>=10:
                                tt = x.split(' ')
                                dd = []
                                for m in range(0,len(tt)):
                                    tt[m] = tt[m]+' '
                                    if '@' in tt[m]:
                                       dd.append(m)
                                for m in range(0,len(dd)):
                                    del tt[dd[m] - m]
                                x = ''.join(tt)
                                if len(x)>0:
                                    count = count + 1
                                    if x[0] == ' ':
                                        x = x[1:]
                                x = x.lower()
                                try:
                                    temp = d[x]
                                except KeyError:
                                    ccount = ccount + 1 
                                    if count%5999 == 0:
                                        print(str(ccount) + '----\n')
                                        print(x)
                                    d[x] = x
print(ccount)
print(count)
print(len(d))
#for i,j in d.items():
#	print(i)
#	print(j)
	



		
