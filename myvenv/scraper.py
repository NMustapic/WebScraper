import urllib.request
from bs4 import BeautifulSoup

get = urllib.request.urlopen("https://www.index.hr")
html = get.read()

soup = BeautifulSoup(html, features="lxml")

# print(soup)

f = open('index.html', 'wb')
f.write(soup.encode("utf-8"))
f.close

mydivs = soup.find_all("a", {"class": "vijesti-text-hover"})

print(mydivs) #ispisiva html kod najvaznijih vijesti

'''for link in soup.find_all('a', href=True):
    print(link['title']+ " " +link['href'])''' #kod za traženje linkova u sveukupnom HTML kodu




