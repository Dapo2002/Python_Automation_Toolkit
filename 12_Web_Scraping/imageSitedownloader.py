# A high-level browser automation script utilizing Selenium to perform targeted 
# keyword searches and navigate complex nested UI modals for media acquisition.

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#  Open the browser, loads the photo site and searches for a photo
browser = webdriver.Edge()
browser.get('https://www.pixabay.com')
time.sleep(2)
search = browser.find_element(By.NAME, 'search')
search.send_keys(' '.join(sys.argv[1:]), Keys.ENTER)
time.sleep(2)

#  Selects images to be downloaded
images = browser.find_elements(By.CSS_SELECTOR, 'img[src*="cdn.pixabay.com/photo/"]')

for image in images[:5]:
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", image)
    image.click()
    time.sleep(1)
    downloadButton = browser.find_elements(By.XPATH, "//span[normalize-space()='Download']")[0]
    browser.execute_script('arguments[0].scrollIntoView({block: "center"})', downloadButton)
    downloadButton.click()
    time.sleep(1)
    download = browser.find_elements(By.XPATH, "//span[normalize-space()='Download']")[1]
    browser.execute_script('arguments[0].scrollIntoView({block: "center"})', download)
    download.click()
    time.sleep(5)
    browser.back()
time.sleep(5)
