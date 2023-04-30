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
# driver.get(f"https://www.tiktok.com/")
# driver.get(f"https://www.tiktok.com/login/phone-or-email/email")
#
# driver.find_element(by='xpath', value='//*[@id="loginContainer"]/div[1]/form/div[1]/input').send_keys(
#     'alphaoumardev@outlook.com')
# driver.find_element(by='xpath', value='//*[@id="loginContainer"]/div[1]/form/div[2]/div/input').send_keys(
#     'Bonjouroumar200@')
driver.refresh()
# time.sleep(20)
# driver.find_element(by='xpath', value='//*[@id="loginContainer"]/div[1]/form/button').click()
# driver.get(f"https://www.tiktok.com/")
# driver.implicitly_wait(43)
# Login
# driver.find_element(by='xpath', value='//*[@id="login-modal"]/div[2]').click()
# driver.find_element(by='xpath', value='//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/button').click()
with open('tiktok.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tag', 'Channel'])

    driver.get(f"https://www.tiktok.com/")
    time.sleep(20)
    try:
        for tag in tags:
            driver.get(f"https://www.tiktok.com/search/user?q={tag}&t=1682423555521")
            time.sleep(10)
            driver.refresh()
            # try:
            #     driver.find_element(by='xpath', value='//*[@id="verify-bar-close"]').click()
            #     driver.refresh()
            #     # Login
            #     # driver.find_element(by='xpath',value='//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/button').click()
            # except:
            #     print("The popup is bloking the page")
            # time.sleep(2)
            last_height = driver.execute_script('return document.documentElement.scrollHeight')
            while True:
                driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
                time.sleep(2)
                new_height = driver.execute_script('return document.documentElement.scrollHeight')
                if new_height == last_height:
                    break
                last_height = new_height
                for i in range(1, 50):
                    try:
                        driver.find_element(by='xpath',
                                            value='//*[@id="tabs-0-panel-search_account"]/div[{}1]/button'.format(
                                                i)).click()
                        time.sleep(2)
                    except:
                        continue
                    try:
                        for n in range(0, 500):
                            try:
                                channel_elements = driver.find_element(by='xpath',
                                                                       value='//*[@id="search_user-item-user-link-{}"]/a[1]'.format(
                                                                           n)).get_attribute('href')
                                writer.writerow([tag, channel_elements])
                            except Exception as e:
                                print("404", e)
                    except:
                        break
    except Exception as e:
        print(e)
