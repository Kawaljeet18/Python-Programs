# To Get The Text From a website and make it readable
# A SHORT SIMPLE PROGRAM TO FETCH THE TEXT ON A WEBPAGE IN A READABLE FORMAT(WITHOUT HTML TAGS)


import requests
from bs4 import BeautifulSoup
base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")
Content = soup.find_all(class_= "content-section")
ttl = []
for row in Content:
    print(row.text)
