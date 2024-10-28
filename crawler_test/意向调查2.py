from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


driver = webdriver.Chrome()

url = "https://www.wjx.cn/vm/exppIBc.aspx#"


def task():
    driver.get(url)
    time.sleep(1)

    topic1_ele_list = driver.find_elements(
        By.XPATH, "//div[@topic='1']//div[@class='ui-radio']"
    )

    topic1_ele = topic1_ele_list[random.randint(0, len(topic1_ele_list) - 1)]
    topic1_ele.click()

    time.sleep(1)

    topic2_input_ele = driver.find_element("//input[@verify='学号']")
    topic2_input_ele.send_keys("20190000000")


task()
