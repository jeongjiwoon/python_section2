from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('cp949')
soup = BeautifulSoup(res, "html.parser")


#print('soup',soup.prettify())

top6 = soup.select("#frgn_deal_tab_0 > tr")

i =1
for e in top6:
    if e.find("a") is not None:
        print("외국인 순매수", e.find("a").string)
        i += 1

top10 = soup.select("#siselist_tab_7 > tr")
for e in top10:
    if e.find("a") is not None:
        print("시가총액상위", e.select_one(".tltle").string)
