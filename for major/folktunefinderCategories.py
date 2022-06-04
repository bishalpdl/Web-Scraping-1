import os
import requests
from bs4 import BeautifulSoup

#for categories
categories = ['Reel', 'Jig', 'Hornpipe', 'Polka', 'Waltz', 'Strathspey',
              'Double jig', 'March', 'Air','Slip jig', 'Polska', 'Slide']

for a in categories:
    path = 'categories'
    filePath = os.path.join('', path+'\\')
    
    #creating directory and files 
    try:
        f = open(filePath+a+'.txt','a')
        f.write('')
        f.close()
    except:
        os.path.join("/",path)
        os.mkdir(path)
        
        f = open(filePath+'Slide.txt','a')
        f.write('')
        f.close()
             
    # from page 1 to page 3 each to 15 datapoint
    for i in range(1,4):
        url = 'http://www.folktunefinder.com/tunes?features=Rhythm%3A'+a+'&page='+str(i)    
        
        page = requests.get(url)
        
        soup = BeautifulSoup(page.text, 'lxml')
        div = soup.find("div", class_= "col-md-9")
        tunes = div.find('ul').find_all("li")
        for tune in tunes:
            print(tune.a.string)
            
            site = 'https://www.folktunefinder.com'+tune.a["href"]
            sitePage = requests.get(site)
            siteSoup = BeautifulSoup(sitePage.text, 'lxml')
            
            # store data in same named file as tune name
            f = open(filePath+a+'.txt','a')
            f.write(siteSoup.find('pre').string)
            f.write('\n\n\n\n')
            f.close()
    


    








        
        

