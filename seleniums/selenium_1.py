import csv
import time

from scrapy.http import cookies
# from scripts.python模拟键盘鼠标操作 import MyLibrary
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# from seleniums.selenium_mouseandkeyboard import MyLibrary

# all_user_pool = [{"13451728020@163.com": "81762371lbj123"}]
all_user_pool = [{"alphaoumardev@outlook.com": "bonjouroumar200"}]


def choose_user(user_index=0):
    global user_login, pwd_login
    for k, v in all_user_pool[user_index]:
        user_login, pwd_login = k, v
    return user_index, user_login, pwd_login


# 后续user池选择
print('Open Chromedriver')

nox_login_brand = "https://cn.noxinfluencer.com/login?userType=brand&service=https%3A%2F%2Fcn.noxinfluencer.com%2F"


def check_ban():
    try:
        driver.find_element(By.CSS_SELECTOR, 'div[class="content confirm"]')
        error_tips = {'1000': '已被反爬办了'}
        return error_tips
    except NoSuchElementException:
        success_tips = {'999': 'get访问成功,未被ban'}
        return success_tips


def driver_get(url):
    """如果需要用封装好用于thread"""
    return driver.get(url)


def start_driver():
    print('Driver initialization...')
    try:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome()
        return options, driver
    except Exception as e:
        print('The broswer has NOT started:', e)


def nox_login(url=nox_login_brand, user_login='alphaoumardev@outlook.com', pwd_login='bonjouroumar200'):
    if url == nox_login_brand:
        driver.get(url)  # 会导致阻塞，需要异步或者线程来强停,否则会等待加载再继续
        time.sleep(12)
        frist_handle = driver.current_window_handle  #获取当前窗口句柄
        driver.switch_to.window(frist_handle)  #跳转到此句柄窗口
        user_id = "email"  # 具体的或者re表达式
        pwd_id = "pwd"
        # pwd_id_text = "pwd-text"  #两个input输入框嵌套
        submit_id = "login-submit"

        try:
            user_dw = driver.find_element("id", value=user_id)  # 返回element对象
            user_dw.click()  # 点击，可省略
            user_dw.clear()  # 清空输入，可省略
            user_dw.send_keys(user_login)  # 在输入框输入
            # value_user = user_dw.get_attribute('value')  # .text方法拿不到input的值，用这个查看,具体搜索get_attribute用法
        except Exception as e:
            error_tips = {'1002', 'The username has failed'}
            print(error_tips, e)
            return error_tips
        try:
            pwd_dw = driver.find_element("id", value=pwd_id)
            pwd_dw.click()
            pwd_dw.send_keys(pwd_login)
        except Exception as e:
            error_tips = {'1003', 'The password has failed'}
            print(error_tips, e)
            return error_tips
        try:
            subbutton_dw = driver.find_element(by=By.ID, value=submit_id)
            subbutton_dw.click()
        except Exception as e:
            error_tips = {'1004', 'Login has failed'}
            print(error_tips, e)
            return error_tips

        time.sleep(9)  # 必须等待，否则会导致不生效
        print('You are banned')
        driver.execute_script("window.open('https://cn.noxinfluencer.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA')") #只有script的opend才可stop
        # driver.close()  # 关闭当前
        return cookies
    else:
        print('You are logged In')



# def check_element_exists(xpath):
#     """检查是否存在元素"""
#     try:
#         driver.find_element(xpath)
#     except NoSuchElementException:
#         return False
#     return True


def get_html():
    """获取页面源码以及当前url"""
    html_str = driver.page_source
    url = driver.current_url
    print(url)
    return html_str, url


def save(save_type='mysql', path='', data_row=''):
    """根据情况，默认选择存储"""
    if save_type == 'csv':
        # G:\cyspider\webspider\spyder_web\nox\data\create_noxwh.csv
        with open(r''.format(path), 'a+', newline="",
                  encoding='utf-8') as f:
            writer = csv.writer(f)
        writer.writerow(data_row)  # dta_row为列表或元组类型，也可为单个str
    else:
        # 链接数据库,存储
        pass


if __name__ == '__main__':
    # 1.启动浏览器
    # / html / body / section / section / div / div[2] / div / div[
    #     1] / div / div / div / div / div / div / div / div / table / tbody / tr[1]
    options, driver = start_driver()

    # 2.选取登录用户
    user_index, user_login, pwd_login = choose_user(user_index=0)
    while True:
        # 3.登录  以及登录初始的判断 循环user_index+=1
        nox_login(user_login=user_login, pwd_login=pwd_login)  # 可能也判断是否被ban
        result_tip = check_ban()
        if list(result_tip.keys())[0] == '1000':
            user_index += 1
            # 重新登录
            break

    # 列表页——网红主页url获取
    wh_1 = 'https://cn.noxinfluencer.com/brand/kolRecommend'  # 此页面默认youtube
    driver.get(wh_1)

    time.sleep(15)
    # MyLibrary().keybd_event(27)
    # MyLibrary().keybd_event(27)

    # 列表页find
    # #定位
    whlist_dw_list = driver.find_elements(By.CSS_SELECTOR, 'tr[class="ant-table-row ant-table-row-level-0"]')
    print(len(whlist_dw_list))
    for whlist_dw in whlist_dw_list:
        wh_nox_url = whlist_dw.get_attribute('data-row-key')  # nox网红的具体url  例如UCq-Fj5jknLsUf-MWSy4_brA
        whlist_dw_text = whlist_dw.text
        print(wh_nox_url)
        print(whlist_dw_text)

    # 存储
    print(len(whlist_dw_list))
    with open(r'nox.csv','a+',newline="",encoding='utf-8') as f:  #newline=""保证不出现换行的空行
        writer= csv.writer(f)
        for whlist_dw in whlist_dw_list:
            wh_nox_url=whlist_dw.get_attribute('data-row-key')  #nox网红的具体url  例如UCq-Fj5jknLsUf-MWSy4_brA
            whlist_dw_text=whlist_dw.text
            data_row=whlist_dw_text#具体的值name,youtube粉丝，nox评分,语言/country,tags,
            print(data_row)
    # """
    # T-Series  name
    # 234M      粉丝数
    # 5.00      nox评分
    # 英语      语言
    # 娱乐 音乐 电影 流行音乐  tag
    # 641.65K
    # $ 72 USD
    # 4.58%
    # """
    # writer.writerow(data_row)
    # 根据实际情况，使用mysql存储更好，便于处理和修改某条数据，后续再导出为excel

    # 根据实际情况，选择另开一个爬虫，爬取具体主页的剩余信息，并追加
    # 点击下一页，这里使用输入
    defalut_index_input = 1  # 用于最下方输入，以及记录爬取到第几页了

    try:
        # 单个详情页
        wh_2='https://cn.noxinfluencer.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA'
        driver.get(wh_2)
    except TimeoutError as e:
        raise e
        # MyLibrary().keybd_event(27)  #设置超过加载时间就强停
    # 详情页find

    time.sleep(0.1)
    get_html()

    time.sleep(30)
    # driver.quit() #关闭所有窗口
    # 无限循环
    while True:
        qs = inputs = 'qs:'
        if qs == 'qs':
            break
