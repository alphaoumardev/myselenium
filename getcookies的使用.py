# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/16 13:39
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : selenium_baidu.py
# @Software: PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # implicitly_wait():隐式等待
driver.get('https:\\www.baidu.com')
# 获取所有的 cookies
print(driver.get_cookies())  # 原始的 cookies  见输出结果 1
driver.add_cookie({"name": "name", "value": "value"})
# 再次获取cookies
print(driver.get_cookies())  # 这时候的 cookies 多了一个我们所添加的  见输出结果2
# 清空所有的 cookie值
driver.delete_all_cookies()
# 再次获取cookies
print(driver.get_cookies())  # 这时候的 cookies 为空 见输出结果3

"""
输出结果:
1、[{'domain': '.baidu.com', 'httpOnly': False, 'name': 'H_PS_PSSID', 'path': '/', 'secure': False, 'value': '1996_1449_28777_21086_28775_28724_28837_28584_26350_28603_22157'}, {'domain': '.baidu.com', 'httpOnly': False, 'name': 'delPer', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.baidu.com', 'expiry': 3703659520.553176, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '4A3A8AC597744EED20AF2E7B47FD98C3:FG=1'}, {'domain': '.baidu.com', 'expiry': 3703659520.553272, 'httpOnly': False, 'name': 'PSTM', 'path': '/', 'secure': False, 'value': '1556175874'}, {'domain': '.baidu.com', 'expiry': 3703659520.55323, 'httpOnly': False, 'name': 'BIDUPSID', 'path': '/', 'secure': False, 'value': '4A3A8AC597744EED20AF2E7B47FD98C3'}, {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'BD_HOME', 'path': '/', 'secure': False, 'value': '0'}, {'domain': 'www.baidu.com', 'expiry': 1557039874, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/', 'secure': False, 'value': '12314753'}]
2、[{'domain': '.baidu.com', 'httpOnly': False, 'name': 'H_PS_PSSID', 'path': '/', 'secure': False, 'value': '1996_1449_28777_21086_28775_28724_28837_28584_26350_28603_22157'}, {'domain': '.baidu.com', 'httpOnly': False, 'name': 'delPer', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.baidu.com', 'expiry': 3703659520.553176, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '4A3A8AC597744EED20AF2E7B47FD98C3:FG=1'}, {'domain': '.baidu.com', 'expiry': 3703659520.553272, 'httpOnly': False, 'name': 'PSTM', 'path': '/', 'secure': False, 'value': '1556175874'}, {'domain': '.baidu.com', 'expiry': 3703659520.55323, 'httpOnly': False, 'name': 'BIDUPSID', 'path': '/', 'secure': False, 'value': '4A3A8AC597744EED20AF2E7B47FD98C3'}, {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'BD_HOME', 'path': '/', 'secure': False, 'value': '0'}, {'domain': 'www.baidu.com', 'expiry': 1557039874, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/', 'secure': False, 'value': '12314753'}, {'domain': 'www.baidu.com', 'expiry': 2186895874, 'httpOnly': False, 'name': 'name', 'path': '/', 'secure': True, 'value': 'value'}]
3、[]
"""