from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import csv

html = urlopen("https://www.cnet.com/reviews/")
bsObj = BeautifulSoup(html)
x=bsObj.findAll('li')
for i in x:
    if i.getText()=='Cars':
        a=i.find('a')
        new="https://www.cnet.com"+a['href']
### Cars category has been selected from the list of the categories        
new_html=urlopen(new)   
bsObj1=BeautifulSoup(new_html)
carz=bsObj1.find("a",{"data-style":"see-all"})['href']
navigator="https://www.cnet.com"+carz


### The extractor goes to the See ALL tab.

## From the list of the available cars, each car title and link associated with that the blog/review
links=[]
products_name=[]
j=1
while(True):
    try:
        if j==1:
            toAdd=''
        else:
            toAdd=str(j)
        j=j+1
        bsObj2=BeautifulSoup(urlopen(navigator+toAdd))
        pname=bsObj2.findAll("a",{"class":"col-3 searchItem product"})
       
        for k in pname:
            link="https://www.cnet.com"+k['href']
            links.append(link)
            name=k.find('h3')
            products_name.append(name.getText())
            print(name.getText())
    except AttributeError:
        break
### The results are made in the form of list and csv file is made.       
myList=[[products_name,links]]
for j in range(len(products_name)):
    myList.append([products_name[j],links[j]])
with open(r"C:\Users\Pujitha\Desktop\cnetcarss.csv" %k, "w",newline='',encoding='utf8') as f:
     writer = csv.writer(f, delimiter=',')
     writer.writerows(myList)
    
