# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:12:03 2019

@author: user
"""

import collections

url = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "http://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]

splited_url = [i.split('/')[-1] for i in url]
#print(splited_url)
counter=collections.Counter(splited_url)
counter = counter.most_common(3)

for p in counter:
    print('{} {}'.format(p[0], p[1]))



