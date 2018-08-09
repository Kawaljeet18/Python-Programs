# TO DECODE A WEBPAGE
# THIS PROGRAM WIL BROWSE A WEBSITE USING REQUESTS(A PYTHON LIBRARY)
# IT WILL PARSE THE FILE FOR TEXT UNDER THE CLASS ITEM-TITLE.
# AND IT WILL PRINT THE TEXT LINE BY LINE AS IT IS IN THE WEBPAGE.


import requests
from bs4 import BeautifulSoup
base_url = 'https://www.ndtv.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")
title = soup.find_all(class_="item-title")


# for story_heading in title:
#      if story_heading.a:
#             print(story_heading.a.text.replace("/n"," ").strip())
#        else:
#             print(story_heading.contents[0].strip())


ttl_list = []
for row in title:
    ttl_list.append(row.text)
print(ttl_list)
