#  A little command-line robot (Selenium) that signs into your webmail and delivers
#  the supplied message to whoever you point it at.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

browser = webdriver.Edge()
browser.get('file:///C:/Users/Abdulbadie/OneDrive/User/PycharmProjects/webScraping/localMail.html')
myMail = browser.find_element(By.CSS_SELECTOR, '#loginEmail')
time.sleep(2)
myMail.send_keys('alice@test.local')
time.sleep(2)
myMailPassword = browser.find_element(By.CSS_SELECTOR, '#loginPassword')
myMailPassword.send_keys('alice123')
time.sleep(2)
myMailPassword.submit()
compose = browser.find_element(By.CSS_SELECTOR, '#navCompose')
compose.click()

#  Composing the message
time.sleep(2)
recipientMail = browser.find_element(By.CSS_SELECTOR, '#to')
recipientMail.send_keys('bob@test.local')
time.sleep(2)
subject = browser.find_element(By.CSS_SELECTOR, '#subject')
subject.send_keys(sys.argv[1])
time.sleep(2)
body = browser.find_element(By.CSS_SELECTOR, '#body')
body.send_keys(' '.join(sys.argv[2:]))
time.sleep(2)
body.submit()
checkForSentMessage = browser.find_element(By.CSS_SELECTOR, '#navSent')
checkForSentMessage.click()

time.sleep(5)
