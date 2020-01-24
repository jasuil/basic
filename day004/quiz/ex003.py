# HTML 에서 BABY 이름 찾기
"""
3)
step 1 - https://developers.google.com/edu/python/exercises/baby-names 에서
file download 하여 babynames directory 로 save
step 2 - <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td> 에
match 되는 정규표현식을 이용하여 (rank, boy-name, girl-name) tuples 추출하여
print
"""

import re, sys
import urllib.request

from selenium import webdriver as webDrv

browser = webDrv.Chrome("C:/Users/kosmo04-22/Desktop/webScraping/chromedriver")
browser.get("file:///D:/%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EA%B8%B0%EC%B4%88%EB%B0%98/basic/day004/quiz/google-python-exercises/babynames/baby1990.html")

menus = browser.find_elements_by_css_selector("tbody tr")

pypi = None

for m in menus:
    #if m.text == "PyPI":
    #    pypi = m
    print(m.text)

