from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url=input("which page would you like to check? enter the url: ")
keyword=input("what is your seo keyword?")
keyword=keyword.casefold()
try:
    html=urlopen(url)
except HTTPError as e:
    print(e)
data=BeautifulSoup(html,"html.parser")
def seo_title_found(keyword,data):
    if data.title:
        if keyword.casefold() in data.title.casefold():
            status="found"
        else:
            status="keyword not found"
    return status
def seo_title_stop_words(data):
    words=0
    list_words=[]
    if data.title:
        with open('stopwords.txt','r') as f:
            for line in f:
                if re.search(r'\b' + line.rstrip('\n') + r'\b',data.title.text.casefold()):
                    words+=1
                    list_words.appen(line.rstrip('\n'))
            if words>0:
                stop_words="we found {} stop words in your title. you should consider removing them fomat(words)"
            else:
                 stop_words="we found no stop words in the title. good work" 
    else:
            stop_words="we could not find a title"
print(seo_title_found(keyword,data))
print(seo_title_stop_words(data))




