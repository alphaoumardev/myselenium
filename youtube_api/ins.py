# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# instaURL="https://www.instagram.com/"
# username = ""
# password = ""
#
# driver = webdriver.Chrome()
# driver.get(instaURL)
#
# time.sleep(3)
#
# usernameEntry = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
# usernameEntry.send_keys(username)
#
# passwordEntry = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
# passwordEntry.send_keys(password)
#
# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
#
# time.sleep(30)

import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://www.youtube.com/results?search_query=outdoor+adventures&sp=EgIQAg%253D%253D")

channels = []
results = driver.find_elements(by=By.XPATH, value="//div[@id='contents']//ytd-channel-renderer")
for result in results[:50]:
    channel_name = result.find_element(by=By.XPATH,value=".//a[@id='main-link']/yt-formatted-string").text
    channel_url = "https://www.youtube.com" + result.find_element(by=By.XPATH, value=".//a[@id='main-link']").get_attribute("href")
    channel_subscribers = result.find_element(by=By.XPATH, value=".//yt-formatted-string[contains(@aria-label, 'subscribers')]").\
                         get_attribute("aria-label").split()[0]
    channels.append((channel_name, channel_url, channel_subscribers))

# Save the data in a CSV file
with open('outdoor_adventures.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Channel Name", "Channel URL", "Subscribers"])
    writer.writerows(channels)

# Close the Chrome driver
# driver.quit()
