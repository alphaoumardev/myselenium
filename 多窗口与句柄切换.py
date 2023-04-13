# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/16 17:18
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : 多窗口与句柄切换.py
# @Software: PyCharm
# coding=utf-8
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化

driver.get('https://www.baidu.com')  # 在当前浏览器中访问百度
time.sleep(2)
# print(driver.current_window_handle)# 输出当前窗口句柄（百度）
frist_handle = driver.current_window_handle

# 新开一个窗口，通过执行js来新开一个窗口,访问搜狗
js = 'window.open("https://www.sogou.com");'
driver.execute_script(js)

# 再新开一个窗口，通过执行js来新开一个窗口，访问有道
js = 'window.open("http://www.youdao.com/");'
driver.execute_script(js)

handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
print(handles)  # 输出句柄集合

for handle in handles:  # 切换窗口（切换到有道）
    if handle != frist_handle:
        # driver.switch_to_window(handle)
        driver.switch_to.window(handle)
        # print(driver.current_window_handle)  # 输出当前窗口句柄（有道）
        # driver.find_element_by_id("translateContent").send_keys("selenium")  # 有道翻译selenium
        driver.find_element(By.ID,"translateContent").send_keys("selenium")  # 有道翻译selenium
        # driver.find_element_by_css_selector("button").click()
        driver.find_element(By.CSS_SELECTOR,"button").click()
        # driver.find_element_by_css_selector("[data-rlog='search-popup-close-win']").click()
        # driver.find_element_by_css_selector("[class='close js_close']").click()  # 关闭弹窗
        driver.find_element(By.CSS_SELECTOR,"[class='close js_close']").click()  # 关闭弹窗
        driver.get_screenshot_as_file("D:\windows\\youdao.jpg")  # 截图  可自定义截图后的保存位置(D:\windows)和图片命名(youdao.jpg)
        time.sleep(5)
        break
driver.close()  # 关闭当前窗口（有道）

for handle in handles:  # 切换窗口（切换到搜狗）
    if handle != frist_handle:
        # driver.switch_to_window(handles[-1])  # 此时只剩两个句柄，取最后一个
        driver.switch_to.window(handles[-1])  # 此时只剩两个句柄，取最后一个
        # print(driver.current_window_handle)  # 输出当前窗口句柄（搜狗）
        # driver.find_element_by_id("query").send_keys("selenium")  # 搜狗搜索selenium
        driver.find_element(By.ID,"query").send_keys("selenium")  # 搜狗搜索selenium
        # driver.find_element_by_id("stb").click()
        driver.find_element(By.ID,"stb").click()
        time.sleep(2)  # 等待2s为了截完整搜索结果图
        driver.get_screenshot_as_file("D:\windows\\sougou.jpg")  # 截图  可自定义截图后的保存位置和图片命名
        time.sleep(5)
        break
driver.close()  # 关闭当前窗口（搜狗）

# driver.switch_to_window(frist_handle) #切换回百度窗口
# driver.switch_to_window(handles[0])  # 切换回百度窗口
driver.switch_to.window(handles[0])  # 切换回百度窗口
# driver.find_element_by_id("kw").send_keys("selenium")  # 百度搜索selenium
driver.find_element(By.ID,"kw").send_keys("selenium")  # 百度搜索selenium
# driver.find_element_by_id("su").click()
driver.find_element(By.ID,"su").click()
time.sleep(2)  # 等待2s为了截完整搜索结果图
driver.get_screenshot_as_file("D:\windows\\baidu.jpg")  # 截图  可自定义截图后的保存位置和图片命名
time.sleep(5)
driver.quit()  # 退出浏览器