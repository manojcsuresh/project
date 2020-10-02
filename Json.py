import json
import urllib.request,urllib.error,urllib.parse
add=0
sum=0

url=input('enter the location:')
print('Retrieving',url)
data=urllib.request.urlopen(url)
file=data.read().decode()
print('Retrieved',len(file),'characters')
file=json.loads(file)

for word in file['comments']:
    add=add+int(word['count'])
    sum=sum+1
print('counts:',sum)
print('sum:',add)
