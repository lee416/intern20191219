# -*- coding: utf-8 -*-

# grap HTML PTT
import urllib.request as req

url ="https://www.ptt.cc/bbs/Gossiping/index.html"
# build request Header #### important ####
request= req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})

#open web as request
with req.urlopen(request) as response:
    data= response.read().decode("utf-8")
    
import bs4
root= bs4.BeautifulStoneSoup(data)


# 標題 titles
titles = root.find_all("div", class_="title")  # find title
for title in titles:
    if title.a != None:
        print(title.a.string)
        
# 日期
dates = root.find_all("div", class_="date")  # find 
for date in dates:
    print(date.string)

# 作者
authors = root.find_all("div", class_="author")  # find 
for author in authors:
    print(author.string)

# 內文
    
        
# 看板名
board = root.find("div", class_="board")  # find 
print(board.span.string)














