from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox() # Get local session of firefox
browser.get("https://workflowy.com") # Load page
browser.find_element_by_css_selector('.button--top-right').click()

time.sleep(2)
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("vijaykhandalnitrr@gmail.com")
password.send_keys("vk@#9717")

login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

time.sleep(20)
clickAble_link = browser.find_element_by_xpath('//a[@href="/#/ff9bf0779e54"]')
clickAble_link.click()

time.sleep(20)
clickable_links = browser.find_elements_by_xpath(".//a[contains(@href, '/#/')]")
clickable_links[-1].click()

time.sleep(10)
clickable_links = browser.find_elements_by_xpath(".//a[contains(@href, 'http://www.geeksforgeeks.org')]")
for links in clickable_links:
    links.click()

browser.close()
