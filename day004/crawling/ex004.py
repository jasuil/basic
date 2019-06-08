# scraping

from selenium import webdriver as webDrv

browser = webDrv.Chrome("C:/Users/kosmo04-22/Desktop/webScraping/chromedriver")
browser.get("https://python.org")

menus = browser.find_elements_by_css_selector("#top ul.menu li")

pypi = None

for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)

pypi.click()

