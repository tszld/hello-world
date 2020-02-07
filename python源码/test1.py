#coding=<utf-8>
# import time
# class Clock(object):
#     def __init__(self,hour=0,minute=0,second=0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#     def run(self):
#             self.second +=1
#             if self.second == 60:
#                 self.second = 0
#                 self.minute +=1
#                 if self.minute == 60:
#                     self.minute = 0
#                     self.hour +=1
#     def display(self):
#         a,b,c = str(self.hour),str(self.minute),str(self.second) 
#         if len(a)==1:
#             a = '0'+ a
#         elif len(b)==1:
#             b = '0'+ b
#         elif len(c)==1:
#             c = '0'+ c
#         print("{}:{}:{}".format(a,b,c),end='\r')
    
# clock = Clock(14,5,45)
# while True:
#     time.sleep(1)
#     clock.run()
#     clock.display()

# import math
# class Point(object):
#     def __init__(self,x = 0.0,y = 0.0):
#         self.x,self.y = x,y
#     def Move(self,x1,y1):
#         self.x = x1
#         self.y = y1
#     def Distance(self,X,Y):
#         d =math.sqrt((Y-self.y)**2+(X-self.x)**2)
#         print(d) 
# point = Point(3,4)
# point.Distance(6,8)

# class matlab_player(object):
#     def __init__(self,):


# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import re

# pages=set() #非字典，乃集合也！
# def getlinks(pageurl):
#     global pages
#     html=urlopen("https://baike.baidu.com"+pageurl)
#     soup = BeautifulSoup(html)
#     for link in soup.find_all('a',href=re.compile(r'^(/fenlei/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 newpage=link.attrs['href']
#                 print(newpage)
#                 pages.add(newpage)
#                 getlinks(newpage)
# getlinks("")

# import requests
# from bs4 import BeautifulSoup
# import bs4
# def getHtmlText(url):
#     try:
#         r = requests.get(url,timeout=4)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         print("爬虫失败")
#         return ""
# def fillUnivList(ulist,html):
#     soup = BeautifulSoup(html,'html5lib')
#     for tr in soup.find('tbody').children:
#         if isinstance(tr,bs4.element.Tag):
#             '''
#             因为要用到bs4.element.Tag,所以在开头要导入bs4库，
#             因为tbody的子代中可能会有字符串节点，所以过滤掉。
#             有时直接写成tr('td')，不要迷糊就是。
#             '''
#             tds = tr.find_all('td')
#             ulist.append([tds[0].string,tds[1].string,tds[3].string]) 
#     return ulist
# def printUnivList(ulist,num):
#     print("{:^10}\t{:^6}\t{:^10}".format('排名','学校','分数'))
#     for i in range(num):
#         u = ulist[i]
#         print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
# def main():
#     uinfo = []
#     url = 'http://zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
#     html = getHtmlText(url)
#     fillUnivList(uinfo,html)
#     printUnivList(uinfo,20)

# main()

#淘宝爬虫实例

# def getHTMLText(url):
#     pass

# def parsePage(html,'html5lib'):
#     pass

# def printGoodsList():
#     pass

# def main():
#     goods = '书包'
#     depth = 2
#     start_url = 'https://www.taobao.com/search?q=书包'
#     infolist=[]


from bs4 import BeautifulSoup
import requests
# html = '''
# <html>
#   <head>
#   </head>
#   <body>
#     <h1>Welcome to my page</h1>
#       <p>
#         <strong> girl<em>in</em> </strong> 
#         <i>A</i>
#         <mark>my</mark>
#         <i>123</i>
#         <small>eye</small>
#         <strike>hello world</strike>
#         <u>she</u>
#         <ins>is</ins>
#         <sub>my</sub>
#         <sub>goddess.</sub>oh!my 
#         <sup>goddess</sup>!'Dog for safe'
#         <a href='D:/TheThirdFiles/标准超文本.html'>标准超文本</a>
#       </p>
#   </body>
# </html>'''



def get_htmls_text(url):
    #获取单章的内容并写入章节文件
    r = requests.get(url)
    r.raise_for_status()
    r.encoding='utf-8'
    html = r.text.replace('<br />','\n')
    
    #要用实践去验证该写什么，不要去臆想，错误出于此。
    soup = BeautifulSoup(html,'html5lib')
    novel_content_Tag = soup.find('div',attrs={'id':'content'})
    novel_content = novel_content_Tag.text.replace('chaptererror();','')
    
    with open('太古神王.txt','a',encoding='utf-8') as f:
        f.write(novel_content)
get_htmls_text('https://www.qu.la/book/4140/2585313.html')



def Get_html_text():
    pass
def Parse_html_text():
    pass
def Print_html_text():
    pass
def main():
    pass 
if __name__ = "__main__":
    main()
