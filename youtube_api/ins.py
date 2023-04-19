import time

from selenium import webdriver
from selenium.webdriver.common.by import By

instaURL="https://www.instagram.com/"
username = ""
password = ""

driver = webdriver.Chrome()
driver.get(instaURL)

time.sleep(3)

usernameEntry = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
usernameEntry.send_keys(username)

passwordEntry = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
passwordEntry.send_keys(password)

driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

time.sleep(30)