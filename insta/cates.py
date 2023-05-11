import csv
import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

tags = ['fashion', 'travel']

driver = webdriver.Chrome(options=options)
driver.get(f"https://www.tiktok.com/")
driver.get(f"https://www.tiktok.com/login/phone-or-email/email")

driver.find_element(by='xpath', value='//*[@id="loginContainer"]/div[1]/form/div[1]/input').send_keys(
    '')
driver.find_element(by='xpath', value='//*[@id="loginContainer"]/div[1]/form/div[2]/div/input').send_keys(
    '')
driver.refresh()
time.sleep(20)
driver.find_element(by='xpath', value='//*[@id="loginContainer"]/div[1]/form/button').click()
driver.get(f"https://www.tiktok.com/")
driver.implicitly_wait(43)
# Login
driver.find_element(by='xpath', value='//*[@id="login-modal"]/div[2]').click()
driver.find_element(by='xpath', value='//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/button').click()

with open('tags.txt', mode='r', newline='', encoding='utf-8') as reading, open('cates.csv', mode='a', newline='', encoding='utf-8') as file:
    reader = reading.read().splitlines()
    writer = csv.writer(file)
    writer.writerow(['Tag', 'Profiles'])

    driver.get(f"https://www.tiktok.com/")
    time.sleep(10)
    driver.get("https://www.tiktok.com/@alx.suarez2/video/7227602923918740779")
    time.sleep(10)
    driver.refresh()
    try:
        for tag in tags:
            driver.get(f"https://www.tiktok.com/search/user?q={tag}")
            driver.refresh()
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
                        driver.find_element(by='xpath', value='//*[@id="tabs-0-panel-search_account"]/div[{}1]/button'.format(i)).click()
                    except:
                        continue
                    try:
                        for n in range(0, 500):
                            try:
                                profiles = driver.find_element(by='xpath', value='//*[@id="search_user-item-user-link-{}"]/a[2]/p[1]]'.format(n)).text
                                writer.writerow([tag, profiles])
                            except:
                                print("404")
                    except:
                        break
    except Exception as e:
        print(e)
