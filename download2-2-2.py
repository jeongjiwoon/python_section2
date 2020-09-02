import sys
import io
import urllib.request as dw
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20141124_60%2Fcuhouse1_1416840327518cYWgm_JPEG%2F04.jpg&type=sc960_832"
htmlURL = "http://google.com"

savePath1 ="c://section2/test1.jpg"
savePath2 ="c://section2/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()
saveFile1 = open(savePath1, 'wb')
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)


print("다운로드 완료!")
