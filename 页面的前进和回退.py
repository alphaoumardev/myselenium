# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/16 13:41
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : 页面的前进和回退.py
# @Software: PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.get("https://www.taobao.com/")
driver.get("https://www.qq.com/?fromdefault")
# 这些都是在一个窗口内完成的
# 后退
driver.back()
print(driver.current_url)
time.sleep(2)
# 前进
driver.forward()
print(driver.current_url)
time.sleep(1)
