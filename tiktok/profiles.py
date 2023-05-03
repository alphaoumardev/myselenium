import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.refresh()

with open('cate.csv', mode='r', newline='', encoding='utf-8') as reading, open('profiles.csv', mode='w', newline='',
                                                                               encoding='utf-8') as file:
    reader = csv.reader(reading)
    writer = csv.writer(file)
    writer.writerow(['Tags', 'Platform', 'Avatar', 'Profile Name', 'Profile Url', 'Location', 'Followers Count',
                     'Likes', 'Description', 'Email', '3 Latest Videos Url', '3 Latest Videos Title',
                     '3 Latest videos image'])

    driver.get("https://www.tiktok.com/")
    time.sleep(15)
    driver.get("https://www.tiktok.com/@alx.suarez2/video/7227602923918740779")
    time.sleep(20)
    driver.refresh()

    for row in reader:
        try:
            driver.get(row[1])  # //*[@id="search_user-item-user-link-0"]/a[2]/p[1]
            tag = row[0]
            platform = 'Tiktok'
            try:
                avatar = driver.find_element(By.XPATH,
                                             value='//*[@id="main-content-others_homepage"]/div/div[1]/div[1]/div[1]/span/img').get_attribute(
                    'src')
            except:
                avatar = ''
            try:
                name = driver.find_element(by="xpath",
                                           value='//*[@id="main-content-others_homepage"]/div/div[1]/div[1]/div[2]/h2').text
            except:
                name = ''
            profile_url = driver.current_url
            location = "USA"
            try:
                followers = driver.find_element(by="xpath",
                                                value='//*[@id="main-content-others_homepage"]/div/div[1]/h3/div[2]/strong').text + " Followers"
            except:
                followers = '0 Flollower'
            try:
                likes = driver.find_element(by="xpath",
                                            value='//*[@id="main-content-others_homepage"]/div/div[1]/h3/div[3]/strong').text + ' Likes'
            except:
                likes = '0 Like'
            try:
                description = driver.find_element(by="xpath",
                                                  value='//*[@id="main-content-others_homepage"]/div/div[1]/h2').text
            except:
                description = ''
            try:
                # driver.execute_script("document.getElementById('email').style.display = 'block';")
                email = driver.find_element(by='xpath', value='//*[@id="email"]').get_attribute('href')
            except:
                email = 'N/A'
            try:
                for i in range(1, 3):
                    videos_url = driver.find_elements(by='xpath',
                                                      value='//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div[{}]/div[2]/a'.format(
                                                          i))
                    video_url = [link.get_attribute('href') for link in videos_url[:3]]
            except:
                video_url = []
            try:
                for i in range(1, 3):
                    videos_title = driver.find_elements(by='xpath',
                                                        value='//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div[{}]/div[2]/a'.format(
                                                            i))
                    video_title = [title.get_attribute('title') for title in videos_title[:3]]
            except:
                video_title = []
            try:
                for i in range(1, 3):
                    videos_image = driver.find_elements(by='xpath',
                                                        value='//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div[{}]/div[1]/div/div/a/div/div[1]/img'.format(
                                                            i))
                    video_image = [image.get_attribute('src') for image in videos_image[:3]]
            except:
                video_image = []
            try:
                other_links = driver.find_elements(by='xpath',
                                                   value='//*[@id="main-content-others_homepage"]/div/div[1]/div[2]/a')
                other_link = [url.get_attribute('href') for url in other_links]
            except:
                other_link = ''

            # Write the data to the CSV file
            writer.writerow(
                [tag, platform, avatar, name, profile_url, location, followers, likes, description, email, video_url,
                 video_title, video_image, other_link])
        except:
            print(row)
