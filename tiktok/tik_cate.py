import csv
import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

tags = ['fashion', 'travel', 'music', 'gaming', 'cooking', ]

driver = webdriver.Chrome(options=options)
driver.get(f"https://www.tiktok.com/login/phone-or-email/email")
driver.implicitly_wait(5)
driver.find_element(by='xpath', value='//*[@id="loginContainer"]/div[1]/form/div[1]/input').send_keys(
    'alphaoumardev@outlook.com')
driver.find_element(by='xpath', value='//*[@id="loginContainer"]/div[1]/form/div[2]/div/input').send_keys(
    'Bonjouroumar200@')
driver.implicitly_wait(5)
driver.find_element(by='xpath', value='//*[@id="loginContainer"]/div[1]/form/button').click()
# driver.get(f"https://www.tiktok.com/")
# Login
driver.find_element(by='xpath', value='//*[@id="login-modal"]/div[2]').click()
# driver.find_element(by='xpath', value='//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/button').click()
with open('channels.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tag', 'Channel'])

    for tag in tags:
        driver.get(f"https://www.tiktok.com/search/user?q={tag}&t=1682423555521")
        driver.refresh()

        driver.implicitly_wait(15)  # Wait for the page to load
        # time.sleep(15)
        try:
            driver.find_element(by='xpath', value='//*[@id="verify-bar-close"]').click()
            driver.refresh()

            # Login
            driver.find_element(by='xpath',
                                value='//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/button').click()
        except:
            print("The popup is bloking the page")
        time.sleep(2)

        # Click the "Load More" button until all channels are displayed
        while True:
            try:
                # load_more_button = driver.find_element(by='xpath', value='//*[@id="main"]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/button')
                load_more_button = driver.find_element(by='xpath',
                                                       value='//*[@id="tabs-0-panel-search_account"]/div[11]/button')
                load_more_button.click()
                time.sleep(2)
            except:
                break

        channel_elements = driver.find_elements('xpath', '//*[@id="search_user-item-user-link-0"]/a[2]/p[1]')

        channel_names = [elem.text for elem in channel_elements]
        for channel_name in channel_names:
            writer.writerow([tag, channel_name])
    # driver.implicitly_wait(10)
