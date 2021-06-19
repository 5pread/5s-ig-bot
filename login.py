from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = 'C:/Users/Barış/PycharmProjects/instabot/webdriver/chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get("https://www.instagram.com")
driver.implicitly_wait(5)     #add delay for Chromedriver to be fully functional

username = driver.find_element_by_name("username")
username.clear()
username.send_keys("aipostingmemeslikeaboss")

password = driver.find_element_by_name("password")
password.clear()
password.send_keys(f"aiposting")
password.send_keys(Keys.RETURN)



try:
    rmb_logincredits = driver.find_element_by_xpath("//button[normalize-space()='Bilgileri Kaydet']")
    rmb_logincredits.click()
    button = driver.find_element_by_class_name("mt3GC")
    button.click()
except:
    pass

add = driver.find_element_by_class_name("q02Nz _0TPg")
add.click()

searchbox = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Ara']")
    )
)
