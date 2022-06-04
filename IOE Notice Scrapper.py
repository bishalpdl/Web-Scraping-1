from bs4 import BeautifulSoup
import requests

from datetime import datetime
from datetime import timedelta

now = datetime.now()


for page in range(1,5):
    soup = requests.get('https://exam.ioe.edu.np/?page='+str(page)).text
    soup = BeautifulSoup(soup, 'lxml')

    notices = soup.find('table')
    for notice in notices.find_all('span'):
        parent = notice.parent.parent
        notice_time = parent.next_sibling.next_sibling.text
        
        if (now - datetime.strptime(notice_time, "%A, %B %d, %Y")) > timedelta(days = 7):
            break
            
        print(notice.text)
        print('Published on', notice_time)
        print('i.e. ', (now - datetime.strptime(notice_time, "%A, %B %d, %Y")).days, ' days before.')

        print('\n')


input('Press any key to exit')












        
        
