import csv
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.youtube.com/@SampsonBoatCo/about')
base_url = 'https://www.youtube.com/'

driver.maximize_window()

avatar = driver.find_element(by="xpath", value='//*[@id="img"]').get_attribute('src')
name = driver.find_element(by="xpath", value='//*[@id="text"]').text
c_link = base_url + driver.find_element(by="xpath", value='//*[@id="channel-handle"]').text
subscribers_count = driver.find_element(by="xpath", value='//*[@id="subscriber-count"]').text
video_count = driver.find_element(by="xpath", value='//*[@id="videos-count"]/span[1]').text
description = driver.find_element(by="xpath", value='//*[@id="description"]').text
joined = driver.find_element(by="xpath", value='//*[@id="right-column"]/yt-formatted-string[2]/span[2]').text

links = driver.find_elements(by='xpath', value='//*[@id="link-list-container"]')
for i in links:
    videos = driver.find_element(by='xpath', value='//*[@id="link-list-container"]/a').get_attribute('href')

link = driver.current_url

time.sleep(5)
driver.get("https://www.youtube.com/@SampsonBoatCo/videos")

video_links = []
videos = driver.find_elements(by='xpath', value='//*[@id="thumbnail"]')
for video in videos[:3]:
    video_links.append(video.get_attribute('href'))

info = [avatar, name, c_link, subscribers_count, video_count, description, joined, link] + video_links

# //*[@id="thumbnail"]
# write information to CSV file
with open('channel.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Avatar', 'Channel Name', 'Channel Link', 'Description', 'Subscriber Count',
                     'Video Link', 'joined', 'Latest Video 1', 'Latest Video 2', 'Latest Video 3'])
    writer.writerow(info)
    print('hu')
time.sleep(50)
# close Chrome driver
# driver.quit()
