from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

'''
    1、获取排行榜上的所有书籍。
    2、获取每本书籍的所有章节。
    3、获取每本章节的内容。
'''

ua = UserAgent()
headers = {'User-Agent':ua.random}
def get_book_links(url):
    r = requests.get(url,headers = headers)
    r.raise_for_status()
    r.encoding='utf-8'

    list1 = []
    soup = BeautifulSoup(r.text,'html5lib')
    book_Tags = soup.find_all('a',attrs={'target':'_blank'})
    for book_link in book_Tags:
        list1.append('https://www.qu.la'+book_link.attrs['href'])
    return list1














#爬取一本书
#获取书的章节链接，并写入列表
def get_content_links(url):
    #获得html源码
    r = requests.get(url,headers = headers)
    r.raise_for_status()
    r.encoding='utf-8'
    
    #将章节名和章节链接写入列表并去重
    links_list=[]
    soup = BeautifulSoup(r.text,'html5lib')
    book_name = soup.h1.get_text()
    for link in soup.find_all('dd'):
        links_list.append('https://www.qu.la/book/4140/'+link.a.attrs['href'])
    #元素去重
    
    return links_list,book_name


def get_htmls_text(url,book_name):
    #获取单章的内容并写入章节文件
    r = requests.get(url,headers = headers)
    r.raise_for_status()
    r.encoding='utf-8'
    html = r.text.replace('<br />','\n')
    
    #要用实践去验证该写什么，不要去臆想，错误出于此。
    soup = BeautifulSoup(html,'html5lib')
    novel_content_Tag = soup.find('div',attrs={'id':'content'})
    novel_title = soup.h1.text +'\n'
    novel_content = novel_content_Tag.text.replace('chaptererror();','')
    
    with open('{}.txt'.format(book_name),'a',encoding='utf-8') as f:
        f.write(novel_title+novel_content)
    print(novel_title)
    
def main():
    url_books = 'https://www.qu.la/paihangbang/'
    for url in get_book_links(url_books):
        links_list = get_content_links(url)[0]
        book_name = get_content_links(url)[1]
        for link in links_list:
            get_htmls_text(link,book_name)

main()