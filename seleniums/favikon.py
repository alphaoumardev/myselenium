# from datetime import time

import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Set up the Chrome driver
driver = webdriver.Chrome()
driver.get("https://favikon.com/search")
search_box = driver.find_element('xpath', "//input[@id='search']")
search_box.send_keys("fitness influencers")
search_box.send_keys(Keys.RETURN)
wait = WebDriverWait(driver, 10)
results = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='result-container']")))
influencer_elements = results.find_elements('xpath', "//div[@class='influencer']")

influencer_data = []
for influencer in influencer_elements:
    name = influencer.find_element('xpath', ".//h4/a").text
    category = influencer.find_element('xpath', ".//p/span[1]").text
    followers = influencer.find_element('xpath', ".//p/span[2]").text
    influencer_data.append((name, category, followers))

with open("influ.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Category", "Followers"])
    writer.writerows(influencer_data)
