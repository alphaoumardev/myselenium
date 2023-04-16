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
# navigate to the website
driver.get("https://www.noxinfluencer.com/brand/kolRecommend")

# create a CSV file to store the scraped data
with open("influ.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "subscribers", "views", "language", "tags", "avg_views", "estimated_earnings",
                  "engagement_rate"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # loop through the pages and scrape the data
    while True:
        rows = driver.find_elements('xpath', "")

        for row in rows:
            avatar = row.find_element(By.CLASS_NAME, 'img.avatar').get_attribute('src')

            name = row.find_element('xpath', "").text
            subscribers = row.find_element('xpath', "").text
            views = row.find_element('xpath', "").text
            language = row.find_element('xpath', "").text
            tags = [tag.text.strip() for tag in row.find_elements('xpath', "")]
            avg_views = row.find_element('xpath', "").text
            estimated_earnings = row.find_element('xpath', "").text
            engagement_rate = row.find_element('xpath', "").text

            # write the data to the CSV file
            writer.writerow({
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
        next_button = driver.find_element('xpath', '')
        if next_button.get_attribute("class") == "ant-pagination-disabled":
            break
        else:
            next_button.click()

        # close the Chrome driver
        driver.implicitly_wait(5)
        driver.quit()
