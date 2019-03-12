from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument( '-u', '--url', required=True, help="project url")
parser.add_argument('-a', '--amt', required=True, help="bid amount")
parser.add_argument('-t', '--tech', required=True, help="bid lang")
args = parser.parse_args()

customer_satisfication_text = "Please give me chance to solve your problem. And I have single working principle if you want to keep someone happy with your work, then complete his work within time span and according to his needs."

app_link_details = ""

############### Content for difference lang#########################
python_bid_content = "I had more than 3 year of experience with python programming. I had successfully completed so many projects in python." +customer_satisfication_text

wordpress_bid_content = "I had more than 5 year of experience with wordpress developement. I had successfully completed so many projects in wordpress."+customer_satisfication_text

php_bid_content = "I had more than 4 year of experience with php developement. I had successfully completed so many projects in php."+customer_satisfication_text

web_bid_content = "I had more than 6 year of experience with web and rest api developement. I already made so many websites at high scale."+customer_satisfication_text

software_dev_bid_content = "I had more than 3 year of experience in software developement. I already made so many software with scalable architechture."+customer_satisfication_text

android_bid_content = "I had more than 4 year of experience in android developement. I already published 2 android application which have more than 5000+ downloads on google play"+ app_link_details +customer_satisfication_text


tech = args.tech

if tech.lower() == "python" :
    bid_content = python_bid_content
elif tech.lower() == "wordpress":
    bid_content = wordpress_bid_content
elif tech.lower() == "web":
    bid_content = web_bid_content
elif tech.lower() == "php":
    bid_content = php_bid_content
elif tech.lower == "android" :
    bid_content = android_bid_content
else:
    bid_content = software_dev_bid_content

browser = webdriver.Chrome('/usr/local/bin/chromedriver') # Get local session of firefox
browser.get("https://www.freelancer.com/login") # Load page

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("passwd")

username.send_keys("mnjfblogin@gmail.com")
password.send_keys("Vijay123")

login_attempt = browser.find_element_by_id("login_btn")
login_attempt.submit()

time.sleep(2)
browser.get(args.url)

time.sleep(3)
browser.find_elements_by_xpath('//*[@id="projectBrief"]/div[1]/div[2]/a')[0].click()
time.sleep(3)

amtTextField = browser.find_elements_by_xpath(
    '//*[@id="pricing"]/div/div[1]/div/input[1]')[0]

amtTextField[0].send_keys(args.amt)

time.sleep(1)
browser.find_element_by_xpath('//*[@id="place-bid"]')[0].click()
time.sleep(3)

bid_content_input_box = browser.find_element_by_id('proposalDescription')
bid_content_input_box.send_keys(bid_content)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="place-bid-step2"]')[0].click()
time.sleep(3)

browser.find_element_by_xpath('')[0].click()
#web development
browser.close()
