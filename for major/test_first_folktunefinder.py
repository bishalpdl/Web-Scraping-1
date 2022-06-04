import requests
from bs4 import BeautifulSoup

url = 'http://www.folktunefinder.com/tunes?features=&page=1'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
print(soup)

div = soup.find("div", class_= "col-md-9")

print(div.find_all("li")[0].a["href"])
print(div.find_all("li")[0].a["href"])
print(div.find_all("li")[0].a.string)

print('https://www.folktunefinder.com'+link)

tunes = div.find('ul').find_all("li")
for tune in tunes:
    print(tune.a.string)
    
    site = 'https://www.folktunefinder.com'+tune.a["href"]
    sitePage = requests.get(site)
    siteSoup = BeautifulSoup(sitePage.text, 'lxml')
    
    f = open('test.txt','a')
    f.write(siteSoup.find('pre').string)
    f.write('\n\n')
    f.close()

site = 'https://www.folktunefinder.com/tunes/93144'
sitePage = requests.get(site)
siteSoup = BeautifulSoup(sitePage.text, 'lxml')
print(siteSoup.find('pre').string)

f = open('test.txt', 'w')
f.write(siteSoup.find('pre').string)




link = div.find_all("li")[0].a["href"]
pageOfPage = requests('https://www.folktunefinder.com'+link)



# for i in div.find_all("li"):
    









        
        
