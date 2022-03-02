from cmath import nan
import urllib.request
from bs4 import BeautifulSoup

get = urllib.request.urlopen("https://www.index.hr")
html = get.read()

soup = BeautifulSoup(html, features="lxml")

# print(soup)

'''f = open('index.html', 'wb')
f.write(soup.encode("utf-8"))
f.close''' #zapisivamo cjelokupni HTML kod stranice u .html datoteku

#mydivs = soup.find_all("a", {"class": "vijesti-text-hover"})
#print(mydivs) #ispisiva html kod najvaznijih vijesti

nizlinkova=[]
niznaslova=[]
for link in soup.find_all('a', href=True):
    title = link.get_text().lstrip()
    niznaslova.append(title)
    nizlinkova.append(link["href"])
    
br=0
for element in nizlinkova:
    if element[0:4]=="http":
        ispisivanje = True
        for rijec in niznaslova[br]:
            if rijec[-1] =="€" or rijec == "Instagram" or rijec=="Facebook" or rijec=="Oglašavanje" or rijec=="recept":
                ispisivanje = False #bolje pogledati petlju i popraviti uvjete ispisivanja
        if ispisivanje:
            print("------------------------------------------")
            print(niznaslova[br])
            print(element) #svi elementi niza su linkovi sa stranice 
    br+=1
        





