# -*- coding: utf-8 -*-

import random
import requests
from bs4 import BeautifulSoup
url="http://wiki.python.org.tw/The%20Zen%20Of%20Python"
r = requests.get(url) #將此頁面的HTML GET下來
#print(r.text) #印出HTML
soup = BeautifulSoup(r.text,"html.parser") 
#print(soup)
sel = soup.select("#id") # 找不好
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

