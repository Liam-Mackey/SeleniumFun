import time
import datetime
from random import randint
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/path/to/chromedriver')

driver.get("https://www.reddit.com/r/pics/")

links = driver.find_elements_by_class_name('outbound')

myLinkArr = []

for link in links:
	myLinkArr.append(link.get_attribute('href'))



for link in myLinkArr:
	print(link)
	driver.get(link)
	time.sleep(2)
	imgs = driver.find_elements_by_tag_name('img')
	for img in imgs:
		src = img.get_attribute('src')
		fileEnding = src.split('.')[-1]
		name = str(datetime.datetime.now()) + "-" + str(randint(0,1000)) + "." + fileEnding
		urllib.urlretrieve(src, "redditPics/" + name)
driver.close()