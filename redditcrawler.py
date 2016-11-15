import schedule 
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def job():
	driver = webdriver.Chrome('/path/to/chromedriver')

	driver.get("https://news.ycombinator.com/")

	time.sleep(3)

	links = driver.find_elements_by_class_name('storylink')

	with open('frontPageOfHackerNewsOn' + str(datetime.datetime.now()) + '.txt', 'w') as out:
		for link in links:
			out.write(link.text + '\n')
			out.write(link.get_attribute('href') + '\n')
			out.write('--------------------------------------------------------------------------' + '\n')


	driver.close()


schedule.every().day.at('15:39').do(job)


while True:
    schedule.run_pending()
    time.sleep(1)