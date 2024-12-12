import urllib
import requests
from bs4 import BeautifulSoup
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
for i in range(1, 4):
    zii = (input())
    lens = len(zii)
    zi = urllib.parse.quote(zii,encoding = 'utf-8', errors = 'replace')
    res = requests.get("https://baike.baidu.com/item/"+zi,headers=header)
    #https://case.jcme.net.cn/
    sup=BeautifulSoup(res.content,'lxml')
    de=sup.find_all('div',attrs={'class':'lemmaSummary_r4t8D J-summary'})
    d1=sup.find_all('div',attrs={'class':'J-lemma-content'})
    d2=sup.find_all('div',attrs={'class':'para_G3_Os content_cFweI MARK_MODULE'})
    with open(zii+'.txt','w',encoding='utf-8') as f:
        for d in de:
            f.write(d.text)
        for i in d2:
            f.write(i.text)
            f.write('\n')
    f.close()