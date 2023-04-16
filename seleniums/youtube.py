import csv

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

# Set the path to the Chrome driver executable
driver_path = "/usr/local/bin/chromedriver"
# import urllib3
#
# http = urllib3.PoolManager(cert_reqs='CERT_NONE')

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get('https://cn.noxinfluencer.com/login?userType=brand&service=https%3A%2F%2Fcn.noxinfluencer.com%2F')
driver.maximize_window()

# Wait for the page to load
# time.sleep(5)

# Find the email and password input fields and enter the login credentials
email_field = driver.find_element(By.XPATH,
                                  '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[3]/form/div[1]/div/div/div[1]/input')
password_field = driver.find_element(By.XPATH,
                                     '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[3]/form/div[2]/div/div/div[1]/input')
email_field.send_keys('alphaoumardev@qq.com')
password_field.send_keys('bonjouroumar200')
driver.find_element(By.CLASS_NAME, 'auth-button').click()

driver.implicitly_wait(5)
# navigate to the website
driver.get("https://www.noxinfluencer.com/brand/kolRecommend")
# driver.get("https://www.noxinfluencer.com/search/youtube/channel")

# create a CSV file to store the scraped data
with open("influ.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["avatar", "name", "subscribers", "views", "language", "tags",
                  "avg_views", "estimated_earnings", "engagement_rate"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # loop through the pages and scrape the data
    while True:
        rows = driver.find_elements('xpath',
                                    "/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr")

        for row in rows:
            try:
                avatar = row.find_element("xpath", '/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/img').get_attribute('src')
                name = row.find_element('xpath', "/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/span").text
                subscribers = row.find_element('xpath', "/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[2]").text
                views = row.find_element('xpath', "/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/div").text
                language = row.find_element('xpath', "/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[4]").text
                tags = [tag.text.strip() for tag in row.find_elements('xpath', "/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/div")]
                avg_views = row.find_element('xpath', "/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/div").text
                estimated_earnings = row.find_element('xpath', "/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[7]").text
                engagement_rate = row.find_element('xpath', "/html/body/section/section/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/div").text
            except StaleElementReferenceException as e:
                print(e)
            # write the data to the CSV file
            writer.writerow({
                "avatar": avatar,
                "name": name,
                "subscribers": subscribers,
                "views": views,
                "language": language,
                "tags": tags,
                "avg_views": avg_views,
                "estimated_earnings": estimated_earnings,
                "engagement_rate": engagement_rate
            })

        # check if there is a next page
        # next_button = driver.find_element('xpath', '/html/body/section/section/div/div[2]/div/div[2]/div/ul/li[9]/a')
        # if next_button.get_attribute("class") == "ant-pagination-disabled":
        #     break
        # else:
        # next_button.click()

        # close the Chrome driver
        # driver.implicitly_wait()
        # driver.quit()
