import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/path/to/chromedriver')

driver.get("https://www.facebook.com/")

emailEl = driver.find_element_by_name('email')
emailEl.clear()
emailEl.send_keys('email_goes_here')

passEl = driver.find_element_by_name('pass')
passEl.clear()
passEl.send_keys('password_goes_here')

loginBtn = driver.find_element_by_id('u_0_n')

loginBtn.click()
time.sleep(5)

textArea = driver.find_element_by_name('xhpc_message')

textArea.send_keys('This facebook post was made entirely with a python3 webcrawler script. yournamehere did not do anything manually, his computer now has the ability to post messages on facebook whenever he wants it to. The singularity is coming folks. I for one welcome our new robot overlords. - Sincerly, webcrawler.py')

time.sleep(10)
submitBtn = driver.find_element_by_xpath("//button/span[.=\"Post\"]")

submitBtn.click()

time.sleep(10)


driver.close()