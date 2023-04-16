import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome driver
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
email_field.send_keys('alphaoumardev@outlook.com')
password_field.send_keys('bonjouroumar200')

# Find the login button and click it
driver.find_element(By.CLASS_NAME, 'auth-button').click()
# login_button = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[3]/form/div[4]/div/div"]')
driver.implicitly_wait(5)

# Navigate to the page
driver.get("https://www.noxinfluencer.com/brand/kolRecommend")
driver.implicitly_wait(5)

# Wait for the table to load
with open("influencers.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["Username", "Subscribers", "View rate", "Language", "Category", "Views", "Earnings", "Engagement rate"])

    # loop through each page until there is no more next page button
    while True:
        # get the list table element
        table = driver.find_element("xpath", "//div[@class='ant-table-body']/table")

        # loop through each row in the table and extract the data
        for row in table.find_elements("xpath", ".//tbody/tr"):
            cols = row.find_elements("xpath", ".//td")
            username = cols[0].find_element("xpath", ".//a").text
            subscribers = cols[1].text
            view_rate = cols[2].text
            language = cols[3].text.strip()
            category = [tag.text.strip() for tag in cols[4].find_elements("xpath", ".//a")]
            views = cols[5].text
            earnings = cols[6].text
            engagement_rate = cols[7].text
            writer.writerow([username, subscribers, view_rate, language, category, views, earnings, engagement_rate])

        # check if there is a next page button and click it if there is
        # next_button = driver.find_element("xpath", "//li[@title='Next Page']")
        # if next_button.get_attribute("class") == "ant-pagination-disabled":
        #     break
        # else:
        #     next_button.click()
        #     time.sleep(5)  # wait for the page to load

# Close the browser
# driver.quit()
