# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/16 13:42
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : selenium打开新界面.py
# @Software: PyCharm

from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
#
# # js 执行打开一个新窗口
# driver.execute_script("window.open('https://www.taobao.com')")
# # brower.execute_script("window.open()")  # 打开新的标签页码
# time.sleep(5)


driver.get("https://cn.noxinfluencer.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA")
# brower.execute_script("window.open()")  # 打开新的标签页码
# time.sleep(5)





# driver.execute_script("window.open('https://www.taobao.com')")
# time.sleep(10)