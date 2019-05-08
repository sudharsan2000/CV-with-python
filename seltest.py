from selenium import webdriver
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:\python3.7\Lib\site-packages\selenium\webdriver\chrome\chromedriver')
driver.get('http://http://192.168.43.52/')
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = BeautifulSoup(res,'lxml').text

print (soup)
