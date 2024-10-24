from selenium import webdriver
import time

driver = webdriver.Chrome()


url = "https://www.wjx.cn/vm/exppIBc.aspx#"


def task():
    driver.get(url)
    time.sleep(10)
