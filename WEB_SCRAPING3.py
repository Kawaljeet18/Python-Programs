# DECODE A WEBPAGE AND GRAB ITS TEXT AND WRITE THIS TO A NEW FILE.
# THIS PROGRAMS BROWSE A WEBPAGE FOR TEXT AND GRABS THAT TEXT IN A FILE (NAME_FILE.TXT)
# ITS SIMPLE READABLE CODE BUT VER USEFUL ONE.

import requests
from bs4 import BeautifulSoup


Base_url = "http://www.nytimes.com"
R = requests.get(Base_url)
soup = BeautifulSoup(R.text,"html.parser")
title = soup.find_all(class_="story-heading")


with open("name_file.txt", 'w') as file:
    for story_heading in title:
        file.write(story_heading.text.replace("\n", "").strip()+'\n')
        print(story_heading.text.replace("\n", "").strip()+'\n')