# An automated game-playing agent using Selenium WebDriver to perform a perpetual 
# directional-key rotation (UP-RIGHT-DOWN-LEFT) on the 2048 game's HTML root 
# element.

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element(By.TAG_NAME, 'html')
try:
    while True:
        for key in (Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT):
            htmlElem.send_keys(key)
            time.sleep(0.5)
except KeyboardInterrupt as e:
    print(f'{e} >> Stopped Autoplay')
