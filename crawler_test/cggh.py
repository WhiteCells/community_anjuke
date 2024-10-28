import requests
import json
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class ThreadPool:
    def __init__(self, max_works) -> None:
        self.__max_works = max_works
        self.__exectuor = ThreadPoolExecutor(max_workers=self.__max_works)
        self.__futures = []

    def add_task(self, task, *args, **kwargs) -> None:
        future = self.__exectuor.submit(task, *args, **kwargs)
        self.__futures.append(future)

    def get_results(self) -> list:
        results = []
        for future in as_completed(self.__futures):
            try:
                res = future.result()
                results.append(res)
            except Exception as e:
                print("ThreadPool::get_results Exception: ", e)
        return results

    def shutdown(self) -> None:
        try:
            self.__exectuor.shutdown()
            print("ThreadPool::shutdown")
        except Exception as e:
            print("ThreadPool::shutdown Exception: ", e)


def requests_task():
    # url = "http://61.183.139.103:8081/model/loginUI"
    url = "http://61.183.139.103:8081/student/login"

    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # "Cookie": "JSESSIONID=AE2DA8ECF139870E4986D2D421CE678C",
        # JSESSIONID=5C41EAC5DFFF15FC2DCEC6FAF9DEE825
        # 5C41EAC5DFFF15FC2DCEC6FAF9DEE825
        "Origin": "http://61.183.139.103:8081",
        "Referer": "http://61.183.139.103:8081/model/loginUI",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    data = {"username": "20214511111", "password": "123123213"}

    rsp = requests.post(url, headers=headers, json=data)

    print(rsp.status_code)
    # print(rsp.text)


def selenium_task():
    url = "http://61.183.139.103:8081/model/loginUI"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    while True:
        # username
        name_ele = driver.find_element(By.ID, "username")
        name_ele.clear()
        name_ele.send_keys("20214511111")

        # pwd
        password_ele = driver.find_element(By.ID, "pwd")
        password_ele.clear()
        password_ele.send_keys("123123213")

        # menu
        menu_ele = driver.find_elements(By.ID, "loginMeau")
        menu_ele[0].click()
        # login button
        login_btn_ele = driver.find_element(
            By.XPATH, "//button[@class='layui-btn login_btn']"
        )
        login_btn_ele.click()
        time.sleep(2)


if __name__ == "__main__":
    pool = ThreadPool(10)
    # while True:
    #     pool.add_task(requests_task)

    while True:
        pool.add_task(selenium_task)
