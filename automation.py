from selenium import webdriver
import urllib3
import os

# get current working directory 
path = os.getcwd()

# join the current working directory path with the chromedriver path
chrome_browser = webdriver.Chrome(os.path.join(path,'chromedriver.exe'))

# maximiize the chrome window browser 
chrome_browser.maximize_window()

# give the chrome browser a website to open and automate
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# search button id
button_text = chrome_browser.find_element_by_class_name('btn-default')
print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

# message id to be searched
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()

user_message.send_keys('I am good fam!')

# click the search button
button_text.click()

output_message = chrome_browser.find_element_by_id('display')

assert 'I am good fam!' in output_message.text

# # closes all windows
# chrome_browser.quit()

# closes the window, use twice to make sure
# chrome_browser.close()
# chrome_browser.close()