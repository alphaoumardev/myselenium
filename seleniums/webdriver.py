import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the Chrome driver executable
driver_path = "/usr/local/bin/chromedriver"

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get('https://cn.noxinfluencer.com/login?userType=brand&service=https%3A%2F%2Fcn.noxinfluencer.com%2F')

# Wait for the page to load
# time.sleep(5)

# Find the email and password input fields and enter the login credentials
email_field = driver.find_element(By.XPATH,
                                  '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[3]/form/div[1]/div/div/div[1]/input')
password_field = driver.find_element(By.XPATH,
                                     '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[3]/form/div[2]/div/div/div[1]/input')
email_field.send_keys('alphaoumardev@outlook.com')
password_field.send_keys('bonjouroumar200')

# Find the login button and click it
driver.find_element(By.CLASS_NAME, 'auth-button').click()
# login_button = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[3]/form/div[4]/div/div"]')

# Wait for the login to complete and the dashboard page to load
# time.sleep(5)
driver.implicitly_wait(5)

url = 'https://www.noxinfluencer.com/brand/kolRecommend'
# Navigate to the influencer recommendations page
driver.get(url)

# Wait for the page to load
# time.sleep(10)
driver.implicitly_wait(5)

# with open("influencers.csv", "w", newline="", encoding="utf-8") as csvfile:
#     fieldnames = ["name", "subscribers", "views", "language", "tags", "avg_views", "estimated_earnings",
#                   "engagement_rate"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
# driver.implicitly_wait(5)

# Scrape the data of all influencers with multiple pages
influencer_data = []
while True:
    # Find all influencer cards on the page
    influencer_cards = driver.find_elements(By.XPATH, "//tbody/tr[@class='ant-table-row ant-table-row-level-0']")

    # influencer_cards = driver.find_elements(By.XPATH,
    #                                         '/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]')

    # Extract the data from each influencer card and add it to the list
    for row in influencer_cards:
        avatar = row.find_element(By.XPATH, ".//img[@class='avatar'").get_attribute('src')

        name = row.find_element(By.XPATH, ".//td[1]/a/span[@class").text
        subscribers = row.find_element(By.XPATH, ".//td[2]").text
        views = row.find_element(By.XPATH, ".//td[3]/div").text
        language = row.find_element(By.XPATH, ".//td[4]").text
        tags = [tag.text.strip() for tag in row.find_elements(By.XPATH, ".//td[5]//a[@class='tag']")]
        avg_views = row.find_element(By.XPATH, ".//td[6]/div").text
        estimated_earnings = row.find_element(By.XPATH, ".//td[7]").text
        engagement_rate = row.find_element(By.XPATH, ".//td[8]/div").text
        # Extract name
        # name = card.find_element(By.TAG_NAME, 'img.avatar > span').text
        #
        # # Extract subscribers
        # subscribers = card.find_element(By.CLASS_NAME,
        #                                 'td.ant-table-column-has-actions ant-table-column-has-sorters ant-table-row-cell-break-word').text
        #
        # # Extract views
        # views = card.find_element(By.CLASS_NAME, 'td.ant-table-row-cell-break-word ').text  # div
        #
        # # Extract language
        # language = card.find_element(By.CLASS_NAME, 'td.ant-table-row-cell-break-word').text
        #
        # # Extract category
        # category = card.find_element(By.CLASS_NAME, 'td.ant-table-row-cell-break-word > div.tags > a.tag').text
        #
        # price = card.find_element(By.CLASS_NAME,
        #                           'td.ant-table-row-cell-break-word > div.ant-table-row-cell-break-word').text
        # pourcentage = card.find_element(By.CLASS_NAME, 'td.ant-table-row-cell-break-word > div').text

        # Add the data to the list
        # influencer_data.append([avatar, name, subscribers, views, language, category, pourcentage, price])

    # Find the "Next" button and click it, if it is enabled
    # try:
    #     next_button = driver.find_element(By.XPATH,
    #                                       '/html/body/section/section/div/div[2]/div/div[2]/div/ul/li[9]')  # + li:not(.disabled)
    #     if not next_button:
    #         break
    #     next_button.click()
    # except Exception as e:
    #     print(e)
    # time.sleep(5)
    # driver.implicitly_wait(5)
    #
    # # Save the data to a CSV file
    with open('influ.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['avatar', 'Name', 'Subscribers', 'Views', 'language', 'category', 'price', 'Engagement Rate'])
        writer.writerows(influencer_data)

    # Close the browser window
    # driver.quit()
    # driver.implicitly_wait(5)
