# crawling

import urllib.request, re

web = urllib.request.urlopen("http://python.org")

html = web.read()

code = str(html).encode("utf-8").decode("cp949")

# <title> 태그가 1개 이상
result = re.compile(r'.*?<title.*?>(.*)</title>', re.I | re.S) #두 개의 플래그 설정
#re.I = ingnore

print(result.findall(code))
#print(html)

web.close()