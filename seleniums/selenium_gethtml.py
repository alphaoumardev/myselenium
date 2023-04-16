# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/16 17:22
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : selenium_gethtml.py
# @Software: PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(10)
pag1=driver.page_source
print(pag1)
driver.close()

