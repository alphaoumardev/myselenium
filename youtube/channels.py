import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--disable-cookies')
# df = pd.read_excel('bookid.xlsx', )
# channels_id = df['IDS'].tolist()
# channel_usernames = ['javascriptmastery', 'mohamed_hoblos', 'CodingWithDawid', 'FoxNews', 'IdrissJAberkane']
# categories = ['sport', 'Arcade', 'Board']
driver = webdriver.Chrome(options=options,)
driver.maximize_window()

with open('ids.csv', 'r', encoding='utf-8') as ide, open('draft.csv', 'w', newline='', encoding='utf-8') as file:
    reader = csv.reader(ide)
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(
        ['Tags', 'Platform', 'Avatar', 'Channel Name', 'Channel Url', 'Location', 'Subscribers Count',
         'Video count', 'Description', 'joined', 'Views', 'Email', '3 Latest Videos Url',
         '3 Latest Videos Title', '3 Latest videos image', 'Other Links', 'Link Title'])
    for row in reader:
        try:
            driver.get(f'https://www.youtube.com/channel/{row[1]}/about')
            driver.refresh()

            tag = row[0]
            platform = 'Youtube'
            try:
                avatar = driver.find_element(By.XPATH, value='//*[@id="img"]').get_attribute('src')
            except:
                avatar = ''
            try:
                name = driver.find_element(by="xpath", value='//*[@id="text"]').text
            except:
                name = ''
            try:
                channel_url = driver.current_url
            except:
                channel_url = ''
            try:
                location = driver.find_element(by='xpath',  value='//*[@id="details-container"]/table/tbody/tr[2]/td[2]').text
            except:
                location = "USA"
            try:
                subscribers_count = driver.find_element(by="xpath", value='//*[@id="subscriber-count"]').text
            except:
                subscribers_count = ''
            try:
                video_count = driver.find_element(by="xpath", value='//*[@id="videos-count"]/span[1]').text
            except:
                video_count = ''
            try:
                description = driver.find_element(by="xpath", value='//*[@id="description-container"]').text
            except:
                description = ''
            try:
                joined = driver.find_element(by="xpath",
                                             value='//*[@id="right-column"]/yt-formatted-string[2]/span[2]').text
            except:
                joined = 'few years ago'
            views = driver.find_element(by='xpath', value='//*[@id="right-column"]/yt-formatted-string[3]').text
            try:
                # driver.execute_script("document.getElementById('email').style.display = 'block';")
                email = driver.find_element(by='xpath', value='//*[@id="email"]').get_attribute('href')
            except:
                email = 'N/A'
            driver.implicitly_wait(2)

            driver.get(f'https://www.youtube.com/channel/{row[1]}/videos')
            driver.refresh()
            driver.implicitly_wait(3)

            # The latest videos url
            try:
                latest_videos_url = driver.find_elements(by='xpath', value='//*[@id="video-title-link"]')
                latest_video_url = [video.get_attribute('href') for video in latest_videos_url][:3]
            except:
                latest_video_url = ['']
            try:
                # The latest videos title
                latest_videos_title = driver.find_elements(by='xpath', value='//*[@id="video-title"]')
                latest_video_title = [title.get_attribute('aria-label') for title in latest_videos_title[:3]]
            except:
                latest_video_title = ['']
            try:
                # The latest videos image
                latest_videos_image = driver.find_elements(by='xpath', value='//*[@id="thumbnail"]/yt-image/img')
                latest_video_image = [image.get_attribute('src') for image in latest_videos_image[:3]]
            except:
                latest_video_image = ['']
            # Write the data to the CSV file
            try:
                other_links = driver.find_elements(by='xpath', value='//*[@id="secondary-links"]/a')
                other_link = [url.get_attribute('href') for url in other_links]
                other_title = [title.get_attribute('title') for title in other_links]
            except:
                other_title = ''
                other_link = ''
            # Write the data to the CSV file
            writer.writerow(
                [tag, platform, avatar, name, channel_url, location, subscribers_count, video_count,
                 description, joined, views, email, latest_video_url, latest_video_title,
                 latest_video_image, other_link,
                 other_title])  # latest_video_urls[0], latest_video_urls[1], latest_video_urls[2]
            driver.implicitly_wait(5)
        except:
            print(row)

# driver.quit()
