from bs4 import BeautifulSoup
import requests

url = 'http://roaringjelly.org/~jc/cgi/abc/find.cgi?P=.*&find=FIND&m=title&W=wide&scale=0.65&limit=50&thresh=5&fmt=single&V=1&Tsel=tune&Nsel=0'

page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')


form = soup.find("form", class_ = "match")
table = form.find('table', class_ = 'match')


lengthOfTable = len(table.find_all('tr'))

checkTitle =''
title = ''
for i in range(2, 4):  #final range = lengthOfTable
    data = table.find_all('tr')[i]
    title = data.find_all('td')[-1].string
    print(title  + '\n')
    
    if(checkTitle == title):
        pass
    else:    
        urlStringConcat = 'http://roaringjelly.org/~jc/cgi/abc/get.cgi?F=ABC&U='
        abcUrl = data.find_all('td')[4].find('a')["href"]
        abcUrl = abcUrl.split('U=')[1]
        finalUrl = urlStringConcat + abcUrl
        print(finalUrl +'\n\n\n\n')
        title = data.find_all('td')[-1].string
        abcPage = requests.get(finalUrl)
        abcSoup = BeautifulSoup(abcPage.text,'lxml')
        
        abc = abcSoup.find("pre")
        # print(abc)

    










