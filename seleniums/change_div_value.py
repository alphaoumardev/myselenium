from selenium.webdriver.common.by import By


def add_attribute(driver, element_obj, attribute_name, value):
    driver.execute_script("arguments[0].%s=arguments[1]" % attribute_name, element_obj, value)


def set_attribute(driver, element_obj, attribute_name, value):
    driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", element_obj, attribute_name, value)


def get_attribute(element_obj, attribute_name):
    return element_obj.get_attribute(attribute_name)


def remove_attribute(driver, element_obj, attribute_name):
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",
                          element_obj, attribute_name)


if __name__ == '__main__':
    from selenium import webdriver

    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome()

    driver.get('https://www.baidu.com')

    # element_obj = driver.find_element_by_xpath('//*[@id="su"]') #selenium版本低于4
    element_obj = driver.find_element(By.XPATH,'//*[@id="su"]')

    js = 'arguments[0].setAttribute(arguments[1],arguments[2])'

    driver.execute_script(js, element_obj, 'value', '就不点击')