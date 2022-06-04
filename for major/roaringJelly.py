from bs4 import BeautifulSoup
import requests

f = open('roaringdata.txt','w')
f.write('')
f.close()

#limit=160 to be incremented to 10000
url = 'http://roaringjelly.org/~jc/cgi/abc/find.cgi?P=.*&find=FIND&m=title&W=wide&scale=0.65&limit=160&thresh=5&fmt=single&V=1&Tsel=tune&Nsel=0'
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

form = soup.find("form", class_ = "match")
for table in form.find_all('table', class_ = 'match'):
    lengthOfTable = len(table.find_all('tr'))
    
    checkTitle =''
    title = ''
    for i in range(2, lengthOfTable-1):  #final range = lengthOfTable-1
        data = table.find_all('tr')[i]
        title = data.find_all('td')[-1].string
        print(title  + '\n')
        
        
        urlStringConcat = 'http://roaringjelly.org/~jc/cgi/abc/get.cgi?F=ABC&U='
        abcUrl = data.find_all('td')[4].find('a')["href"]
        abcUrl = abcUrl.split('U=')[1]
        finalUrl = urlStringConcat + abcUrl
        print(finalUrl +'\n\n\n\n')
        title = data.find_all('td')[-1].string
        abcPage = requests.get(finalUrl)
        abcSoup = BeautifulSoup(abcPage.text,'lxml')
        
        abc = abcSoup.find("pre").string
        f = open('roaringdata.txt','a', encoding="utf-8")
        f.write(abc)
        f.write('\n\n\n')
        f.close()
        # print(abc)

        





# parsing all tables
# from each table url is extracted
# this url is used to get abc format data
# file writting
# Same title data is not implemented 








