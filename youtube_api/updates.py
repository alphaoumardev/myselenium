import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace these with the 5 YouTube channel usernames you want to extract information from
channel_usernames = ['javascriptmastery', 'mohamed_hoblos', 'CodingWithDawid', 'FoxNews', 'IdrissJAberkane']
# s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome()
driver.maximize_window()

# Create a new CSV file to store the data
with open('youtube_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Platform', 'Avatar', 'Channel Name', 'Channel_link', 'Location', 'Subscribers Count', 'Video count', 'Description', 'joined', 'Views', 'Email']) #'Latest Video 1', 'Latest Video 2', 'Latest Video 3'

    # Loop through each channel username and extract information
    for username in channel_usernames:
        # Visit the About page for the channel
        driver.get(f'https://www.youtube.com/@{username}/about')

        # Extract the channel name, subscribers, views, and description
        # try:

        platform = 'Youtube'
        avatar = driver.find_element(By.XPATH, value='//*[@id="img"]').get_attribute('src')
        name = driver.find_element(by="xpath", value='//*[@id="text"]').text
        c_link = driver.current_url
        location = driver.find_element(by='xpath', value='//*[@id="details-container"]/table/tbody/tr[2]/td[2]').text
        subscribers_count = driver.find_element(by="xpath", value='//*[@id="subscriber-count"]').text
        video_count = driver.find_element(by="xpath", value='//*[@id="videos-count"]/span[1]').text
        description = driver.find_element(by="xpath", value='//*[@id="description-container"]').text
        joined = driver.find_element(by="xpath", value='//*[@id="right-column"]/yt-formatted-string[2]/span[2]').text
        views = driver.find_element(by='xpath', value='//*[@id="right-column"]/yt-formatted-string[3]').text
        try:
            driver.execute_script("document.getElementById('email').style.display = 'block';")
            email = driver.find_element(by='xpath', value='//*[@id="email"]').get_attribute('href')
        except Exception as e:
            print(e)
        # channel_name = driver.find_element_by_css_selector('#channel-title').text
        # subscribers = driver.find_element_by_css_selector('#subscriber-count').text
        # views = driver.find_element_by_css_selector('#view-count').text
        # description = driver.find_element_by_css_selector('#description-container').text

        # Extract the URLs for the 3 latest videos
        # latest_videos_image = driver.find_element(by='xpath', value='//*[@id="thumbnail"]/yt-image/img')
        # latest_videos_title = driver.find_elements(by='xpath', value='//*[@id="video-title"]')
        # latest_video_links = [video.get_attribute('href') for video in latest_videos_title][:3]

        # Write the data to the CSV file
        writer.writerow([platform, avatar, name, c_link, location, subscribers_count, video_count, description, joined, views, email,]) #latest_video_links[0], latest_video_links[1], latest_video_links[2]
        driver.implicitly_wait(10)
        # except Exception as e:
        #     raise e
# Close the Chrome driver
# driver.quit()
