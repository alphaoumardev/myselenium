# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/2 14:44
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : 鼠标悬浮操作.py
# @Software: PyCharm
"""
参考
https://blog.csdn.net/Sily_Z/article/details/82663370
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

# ActionChains(driver).move_to_element(driver.find_element_by_link_text("设置")).perform()
ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, "设置")).perform()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "高级搜索").click()
