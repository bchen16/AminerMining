import sys
import requests
import json
import threading as thd
import time

with open('affiliationNames.txt','r') as f:
        lines = list(f.readlines())

i = 7943 
result = []
def query():
    global i
    global result
    if len(lines[i])>2:
        if i<22700:
            lines[i] = lines[i][0:-1]
            response = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?key=AIzaSyDx4h0ZpD7jyAxi8ZQ6HyUjzaYgTdnrBJY&query=' + lines[i])
            tempDic = json.loads(response.content)
            tempStr = json.dumps(tempDic)
            with open("clean_affiliations.txt", "a") as myfile:
                myfile.write(str(lines[i])+ '-----+++++-----'  +tempStr + '\n') 
        else:
            return
    i = i + 1
    thd.Timer(0.025,query).start()
query()
#response = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?key=AIzaSyD8ywRmRVJAbL4EfpO7Bi6yrkTHrLcadDQ&query=\nxerox rochester')
#response_str = response.content
#json1_data = json.loads(response_str)['results']
#for i in json1_data:
#    print()
#    if str(type(i)) == "<class 'dict'>":
#        for k,v in i.items():
#            print(str(k) + ':')
#            print(v)
#    print(temp)
#print(root.tag)
