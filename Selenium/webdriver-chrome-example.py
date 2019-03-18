
#--- Selenium Specific Imports ---#
from selenium import webdriver
from selenium.webdriver import Chrome

#--- Generic Imports ---#
import time


if __name__ == '__main__':
    url = 'http://google.com'
    
    browser = Chrome()
    
    browser.get(url)

    time.sleep(5)

    browser.quit() 