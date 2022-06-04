import requests
from bs4 import BeautifulSoup


url = 'https://abcnotation.com/browseTunes'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find("table", class_ ="width100pc table-bordered")
tableRows = table.find_all('tr')[1]
#should be iterated to all td
for tableData in tableRows.find_all('td'): 
    
    counter = 0
    for firstLink in tableData.find_all('a'):
        try:
            abcWebsite = 'https://abcnotation.com/'
            firstLink =  abcWebsite + firstLink['href']
            
            secondPage = requests.get(firstLink)
            secondSoup = BeautifulSoup(secondPage.text, 'lxml')
            
            checkString = ''
            
            secondSoup.pre.find_all('a')[1]["href"]
            
            for i in secondSoup.pre.find_all('a'):
                try:
                    i["href"]
                    if(i.string != checkString):
                        # # print(i['href'])
                        # print(i.string+'\n')
                        checkString = i.string
                        thirdLink = abcWebsite + i['href']
                        #print(thirdLink)
                        print(counter)
                        counter +=1
                        
                        thirdPage = requests.get(thirdLink)
                        thirdSoup = BeautifulSoup(thirdPage.text, 'lxml')
                        # # print(thirdSoup.find('pre'))
                        
                        f = open('datafromABC2.txt','a')
                        f.write(thirdSoup.find('pre').string)
                        f.write('\n\n\n')
                        f.close()
                        
                        
                            
                        
                except:
                    pass
                
        except:
                pass
        
    
    





