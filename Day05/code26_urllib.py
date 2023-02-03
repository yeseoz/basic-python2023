# urllib 패키지 불러오기
from urllib.request import Request, urlopen

req = Request('https://www.naver.com') # 웹사이트 요청
res = urlopen(req) # 웹사이트에 연결되었는지 확인
print(res.status) # http 코드 200   ##404 나오면 오류##
# internet = 네트워크를 통한 request 와 response

