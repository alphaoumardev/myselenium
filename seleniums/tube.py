import csv

from selenium import webdriver

# create a webdriver instance
driver = webdriver.Chrome()

# navigate to the YouTube channel page
driver.get("https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw")

# get the channel name
channel_name = driver.find_element(by="xpath", value='//h1[contains(@class,"ytd-channel-name")]//yt-formatted-string').text

# get the channel views
channel_views = driver.find_element(by="xpath", value='//span[contains(@class,"ytd-channel-subheader")]//span[1]//yt-formatted-string').text

# get the 3 latest video links
latest_videos = driver.find_elements(by="xpath", value='//div[contains(@class,"ytd-grid-video-renderer")]//a[@id="video-title"]')
video_links = []
for video in latest_videos[:3]:
    video_links.append(video.get_attribute('href'))

# get the number of subscribers
subscribers = driver.find_element(by="xpath", value='//yt-formatted-string[contains(@class,"ytd-subscribe-button-renderer")]//span[1]').text

# get the channel description
channel_description = driver.find_element(by="xpath", value='//div[contains(@class,"ytd-channel-about-metadata-renderer")]//yt-formatted-string').text

# get the channel links
channel_links = driver.find_elements(by="xpath", value='//div[contains(@class,"ytd-channel-about-metadata-renderer")]//a')
links = []
for link in channel_links:
    links.append(link.get_attribute('href'))

# save the data in a CSV file
with open('channel_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Channel Name', 'Channel Views', 'Latest Video Links', 'Subscribers', 'Channel Description', 'Channel Links'])
    writer.writerow([channel_name, channel_views, video_links, subscribers, channel_description, links])

driver.implicitly_wait(10)
# close the webdriver instance
driver.quit()
