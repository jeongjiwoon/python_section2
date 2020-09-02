import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20141124_60%2Fcuhouse1_1416840327518cYWgm_JPEG%2F04.jpg&type=sc960_832"
htmlURL = "http://google.com"

savePath1 ="c://section2/test1.jpg"
savePath2 ="c://section2/index.html"

dw.urlretrieve(imgUrl, savePath1) #저장
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
