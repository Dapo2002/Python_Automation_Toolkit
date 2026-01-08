# A surgical probe utilizing Selenium's 'find_element' method to locate and 
# identify specific DOM nodes by their class attributes, featuring robust error 
# handling for missing elements.

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element(By.CLASS_NAME, 'img-center')
    print('Found <%s> element with that class name!' % elem.tag_name)
except Exception as e:
    print('Was not able to find an element with that name.\n', e)
