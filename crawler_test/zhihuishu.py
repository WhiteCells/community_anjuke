from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
# chrome_options.debugger_address = "127.0.0.1:9222"


def task():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("www.bilibili.com")
    print(driver.title)

    # el-scrollbar__wrap
    list_eles = driver.find_elements(By.XPATH, "//div[@class='el-scrollbar__wrap']//li[@class='clearfix video']")
    # for ele in list_eles:
    for i in range(11, len(list_eles)):
        video_time_str = list_eles[i].find_element(By.XPATH, ".//span[@class='time fl']").text
        print(video_time_str)
        video_time = int(video_time_str.split(":")[1]) + 1
        print(video_time)
        list_eles[i].click()
        time.sleep(3.3)
        driver.find_element(By.XPATH, "//div[@class='videoArea']").click()
        time.sleep(video_time * 60)
    time.sleep(10)


if __name__ == "__main__":
    task()
