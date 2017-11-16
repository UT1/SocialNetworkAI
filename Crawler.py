import requests
import re
from bs4 import BeautifulSoup
import json
from collections import namedtuple
from random import randint
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept-Encoding': ', '.join(('gzip', 'deflate')),
    'Accept': '*/*',
    'Connection': 'keep-alive',
}

class MyQuery:
    dict=[]
    def quote(this,sk):
        rand=(int)(randint(1,15))
        count=0;
        for i in range(1,2):
            url='https://www.goodreads.com/quotes/tag/'+sk+'?page='+str(i);
            response = requests.get(url, headers=headers)
            html = response.content
            soup=BeautifulSoup(html,'lxml')
            soup.prettify()
            for script in soup(["script", "style"]):
                script.extract()
            for row in soup.find_all('div',attrs={"class" : "quoteDetails"}):#This div contains each quote seperately and thus further we extract the below aspects from these
                for k in row.find_all('div',attrs={"class" : "quoteText"}):#To get the quotes
                    a= k.text
                    thumbnails = row.select('img[src]')#To extract thw image url of that particular quote
                    for thumbnail in thumbnails:
                        b= thumbnail['src']
                for like in row.find_all('a',attrs={"class":"smallText"}):#To get the number of likes the quote recieved
                        l=like.text
                for author in row.find_all('a',attrs={"class":"authorOrTitle"}):#To get the author or the title of the
                        au=author.text
                count=count+1;
                if count==rand:
                    return a;
#
# s=MyQuery();
# print s.quote('rain');
