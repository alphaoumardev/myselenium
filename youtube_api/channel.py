import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace these with the 5 YouTube channel usernames you want to extract information from
# channel_usernames = ['javascriptmastery', 'mohamed_hoblos', 'CodingWithDawid', 'FoxNews', 'IdrissJAberkane']
channel_id = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw'
# s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome()
driver.maximize_window()

# Create a new CSV file to store the data
with open('channel.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Platform', 'username', 'Avatar', 'Channel Name', 'Channel Url', 'Location', 'Subscribers Count',
                     'Video count', 'Description', 'joined', 'Views', 'Email', '3 Latest Videos Url', '3 Latest Videos Title', '3 Latest videos image']) #'Latest Video 1', 'Latest Video 2', 'Latest Video 3'

    # Loop through each channel username and extract information
        # Visit the About page for the channel
    try:
        driver.get(f'https://www.youtube.com/@mrbeast/about')
        driver.refresh()
        # driver.find_element(by='xpath', value='//*[@id="tabsContent"]/tp-yt-paper-tab[7]/div/div[1]').click()
        # about_tab = driver.find_element(by='xpath', value="//a[@href='/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/about']")
        # about_tab.click()
        # driver.find_element(By.XPATH, value='//*[@id="tabsContent"]/tp-yt-paper-tab[7]/div').click()
        # driver.refresh()
        # Extract the channel name, subscribers, views, and description
        # try:

        platform = 'Youtube'
        username = driver.find_element(by="xpath",
                                               value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[1]/yt-formatted-string[1]').text
        avatar = driver.find_element(By.XPATH, value='//*[@id="img"]').get_attribute('src')
        name = driver.find_element(by="xpath", value='//*[@id="text"]').text
        channel_url = driver.current_url
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
        driver.implicitly_wait(3)

        current_url = driver.current_url
        new_url = current_url.rsplit('/', 1)[0] + '/videos' # To navigate to the videos by url
        driver.get(new_url)

        # driver.find_element(by=By.XPATH, value='//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div/div[1]').click()
        driver.refresh()
        # The latest videos url
        latest_videos_url = driver.find_elements(by='xpath', value='//*[@id="video-title-link"]')
        latest_video_url = [video.get_attribute('href') for video in latest_videos_url][:3]

        #The latest videos title
        latest_videos_title = driver.find_elements(by='xpath', value='//*[@id="video-title"]')
        latest_video_title = [title.get_attribute('aria-label') for title in latest_videos_title[:3]]

        # The latest videos image
        latest_videos_image = driver.find_elements(by='xpath', value='//*[@id="thumbnail"]/yt-image/img')
        latest_video_image = [image.get_attribute('src') for image in latest_videos_image[:3]]

        # Write the data to the CSV file
        writer.writerow([platform, username, avatar, name, channel_url, location, subscribers_count, video_count, description, joined, views, email, latest_video_url, latest_video_title,  latest_video_image]) #latest_video_urls[0], latest_video_urls[1], latest_video_urls[2]
        driver.implicitly_wait(5)
    except Exception as e:
        print('Not found', e)

# driver.quit()
