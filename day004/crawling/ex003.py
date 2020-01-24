import bs4
import urllib.request as req
import re

url = "http://www.ikosmo.co.kr/"
url2 = "http://www.ikosmo.co.kr/?view=dynamicPage&code=center_intro"
readHtml = req.urlopen(url)
readHtml2 = req.urlopen(url2)
obj = bs4.BeautifulSoup(readHtml,'html.parser')
obj2 = bs4.BeautifulSoup(readHtml2,'html.parser')

#print(obj)
#print(type(obj))
#print(obj2)


divStr = obj.find("div", {"class":"article fl article_short"})
divStr2 = obj2.find("div", {"class":"center_intro"})

#print(divStr2.get_text())
#print(divStr2.text)

#divStr = obj.find("div", {"id":"container"})
#h2Tag = re.findall("[h2]", divStr)



print(divStr2)
#print("div seleted is \n==> \n{}".format(divStr))
