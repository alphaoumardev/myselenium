# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/2 13:50
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : change_div_value.py
# @Software: PyCharm
"""
selenium之UI自动化时更改/添加/获取标签的属性值
在web自动化测试的过程中，根据用例可能需要

①获取某元素的某标签的某属性值；例如使用 get_attribute('value') 获取元素显示的value值

②更改某元素的某标签的某属性值；例如密码框需要先将type属性的属性值由password修改为text之后才可以使用 get_attribute('value')

③增加某元素的某标签的某属性值；（暂时未用到）
"""
from selenium.webdriver.common.by import By


def add_attribute(driver, element_obj, attribute_name, value):
    """
    封装向页面标签添加新属性的方法
    调用JS给页面标签添加新属性，arguments[0]~arguments[2]分别
    会用后面的element，attributeName和value参数进行替换
    添加新属性的JS代码语法为：element.attributeName=value
    比如input.name='test'
    """
    driver.execute_script("arguments[0].%s=arguments[1]" % attribute_name, element_obj, value)


def set_attribute(driver, element_obj, attribute_name, value):
    """
    封装设置页面标签的属性值的方法
    调用JS代码修改页面元素的属性值，arguments[0]~arguments[1]分别
    会用后面的element，attributeName和value参数进行替换
    """
    driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", element_obj, attribute_name, value)


def get_attribute(element_obj, attribute_name):
    # 封装获取页面对象的属性值方法（selenium原生api）
    return element_obj.get_attribute(attribute_name)


def remove_attribute(driver, element_obj, attribute_name):
    """
    封装删除页面标签的属性的方法
    调用JS代码删除页面元素的指定的属性，arguments[0]~arguments[1]分别
    会用后面的element，attributeName参数进行替换
    """
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",
                          element_obj, attribute_name)


if __name__ == '__main__':
    from selenium import webdriver

    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(executable_path='/home/test/MyCode/Common/driver/chromedriver_105',
                              chrome_options=options)

    driver.get('http://www.baidu.com')

    # element_obj = driver.find_element_by_xpath('//*[@id="su"]') #selenium版本低于4
    element_obj = driver.find_element(By.XPATH,'//*[@id="su"]')

    js = 'arguments[0].setAttribute(arguments[1],arguments[2])'

    driver.execute_script(js, element_obj, 'value', '就不点击')