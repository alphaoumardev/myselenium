# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/16 18:22
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : selenium_wait.py
# @Software: PyCharm
#两种等待

import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()

driver.implicitly_wait(5)
time.sleep(5)
# 显示等待与隐式等待的区别
#
# implicitly_wait(5)属于隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时；
#
# time.sleep(5)表示必须等待5秒定位；

#动作等待
wait=WebDriverWait(driver,10)
wait.until(driver.find_element('666'))