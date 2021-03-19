from selenium import webdriver
import os
import time
import functionss
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

path = os.path.abspath(os.getcwd())
driver_path = r'C:\yourpath\driver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://www.instagram.com")
browser.implicitly_wait(10)     #add delay for Chromedriver to be fully functional

username = browser.find_element_by_name("username")
username.clear()
username.send_keys(f"yourname")
password = browser.find_element_by_name("password")
password.clear()
password.send_keys(f"yourpassword")
submit = browser.find_element_by_tag_name('form')
submit.submit()
instagram = browser.find_element_by_class_name("s4Iyt")
instagram.click()
button = browser.find_element_by_class_name("mt3GC")
button.click()
browser.implicitly_wait(10)
searchbox = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Ara']")
    )
)
tags = ['memesdaily', 'memes', 'cursedmemes']
random_tag = random.choice(tags)
browser.get(f"https://www.instagram.com/explore/tags/{random_tag}/")






