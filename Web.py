# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
url="http://wiki.python.org.tw/The%20Zen%20Of%20Python"



from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "hello flask "

if __name__ == "__main__":
    app.run()

