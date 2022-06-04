import requests
from bs4 import BeautifulSoup

f = open('folktune2.txt','w')
f.write('')
f.close()

#from page1 to page10
count = 0
for i in range(1,2000):
    url = 'http://www.folktunefinder.com/tunes?features=&page='+str(i)
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text, 'lxml')
    div = soup.find("div", class_= "col-md-9")
    tunes = div.find('ul').find_all("li")
    for tune in tunes:
        #print(tune.a.string)
        
        site = 'https://www.folktunefinder.com'+tune.a["href"]
        sitePage = requests.get(site)
        siteSoup = BeautifulSoup(sitePage.text, 'lxml')
        
        f = open('folktune2.txt','a')
        f.write(siteSoup.find('pre').string)
        f.write('\n\n\n\n')
        f.close()
        
        print("Number of Scraped datapoint = ", count)
        count += 1





# site = 'https://www.folktunefinder.com/tunes/93144'
# sitePage = requests.get(site)
# siteSoup = BeautifulSoup(sitePage.text, 'lxml')
# print(siteSoup.find('pre').string)

# f = open('test.txt', 'w')
# f.write(siteSoup.find('pre').string)


# link = div.find_all("li")[0].a["href"]
# pageOfPage = requests('https://www.folktunefinder.com'+link)
# for i in div.find_all("li"):
    








        
        
