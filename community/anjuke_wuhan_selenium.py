from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


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


url = "https://wuhan.anjuke.com/community/"

options = Options()


def task():
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # time.sleep(10)

    # 账号密码登录
    # menu_ele = driver.find_element(
    #     By.XPATH, "//div[@class='right-bar']/div[@class='menu']"
    # )
    # menu_ele.click()
    # driver.find_element(
    #     By.XPATH, "//input[@placeholder='请输入用户名/邮箱/手机']"
    # ).send_keys("18871357225")
    # driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']").send_keys(
    #     "1q2w3e4r"
    # )

    # time.sleep(10)
    #

    # 地区
    region_eles = driver.find_elements(By.XPATH, "//li[@class='region-item']/a")

    # 选择地区
    i = 0
    for region_ele in region_eles:
        if i == 0:
            # 跳过 '全部小区'
            continue
        print(region_ele.text)
        region_ele.click()

    # time.sleep(10)

    driver.quit()


if __name__ == "__main__":
    pool = ThreadPool(max_works=10)
    # for i in range(1):
    #     pool.add_task(task)

    task()
