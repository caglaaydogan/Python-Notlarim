import json
import re

f=open("deneme.txt","r")
#print(f.read())

print(f.readline())

degisken=f.readline()
karakter=re.search("\s",degisken)
print(karakter)


a=open("veri.json","r")
b=a.read()
c=json.loads(b)
print(c["isim"])

yas=c["yas"]
if int(yas)>18:
    print("ergen değil")
else:
    print("ergen")



#for i in c:
    #print(i)
