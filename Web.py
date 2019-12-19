# -*- coding: utf-8 -*-

import random
import requests
from bs4 import BeautifulSoup

from lxml import etree

url="http://wiki.python.org.tw/The%20Zen%20Of%20Python"
r = requests.get(url) #將此頁面的HTML GET下來
#print(r.text) #印出HTML
soup0 = BeautifulSoup(r.text,"html.parser") 
soup = BeautifulSoup(r.text,"lxml") 
#print(soup)

a_tags = soup.find_all('a')
for tag in a_tags:
  print(tag.string)

sel = soup.find_all('textarea')
for sele in sel:
  print(sele.string)
  
  
  
print(sel)






for s in sel:
        msg = ()


sentence = random.choice (msg)






from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return sentence # hello

if __name__ == "__main__":
    app.run()

