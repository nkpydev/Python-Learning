#--- Selenium Imports ---#
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#---Generic Imports ---#
import time
#import os
#from os import path


if __name__ == '__main__':
    
    dcaps = DesiredCapabilities.FIREFOX.copy()
    dcaps['marionette'] = False

    browser = webdriver.Firefox(desired_capabilities=dcaps)

    url = 'http://google.com'

    browser.get(url)

    time.sleep(5)

    browser.quit()