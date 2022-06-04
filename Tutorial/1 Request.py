import requests 
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

soup


#tag --- these are html tags e.g. header, div, p, body,
#they are in purple in color
soup.header
soup.div

#navigable String  --- these are string that are rendered

tag = soup.header.span
tag.string

soup.header.p.string


#Attribute --- these are the class,id,role,data-target.... inside html tag         
#these are in yellow color or light blue in html page chrome

tag = soup.header.a.attrs
tag
tag2 = soup.header.a
tag2['data-toggle']

# inserting new attribute
tag = soup.header.a
tag['new_attribute'] = 'This is inserted one'

tag.attrs



# Rough
tag.span.string = "Changed"
tag.span.string

tag

