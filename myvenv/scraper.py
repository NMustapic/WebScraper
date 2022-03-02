import urllib.request
from bs4 import BeautifulSoup

get = urllib.request.urlopen("https://www.index.hr")
html = get.read()

soup = BeautifulSoup(html, features="lxml")

# print(soup)

f = open('index.html', 'wb')
f.write(soup.encode("utf-8"))
f.close #zapisivamo cjelokupni HTML kod stranice u .html datoteku

#mydivs = soup.find_all("a", {"class": "vijesti-text-hover"})
#print(mydivs) #ispisiva html kod najvaznijih vijesti

niz=[]
for link in soup.find_all('a', href=True):
    niz.append(link["href"])
    
for element in niz:
    if element[0:4]=="http":
        print(element) #svi elementi niza su linkovi sa stranice
        
#print(niz)




