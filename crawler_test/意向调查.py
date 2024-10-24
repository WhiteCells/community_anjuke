from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import threading


url = "https://wj.qq.com/s2/15543843/303d/"
options = Options()
# options.add_argument('--headless')


def task():
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(1)
    try:
        while True:
            browser.get(url)

            #

            bath_address = browser.find_element(
                By.XPATH, '//label[@for="q-1-abcd-o-101-EFGH"]'
            )
            bath_address.click()

            # time.sleep(1)

            bath_address_type = browser.find_element(
                By.XPATH, '//label[@for="q-6-T3rh-o-0-nTfR"]'
            )
            bath_address_type.click()

            # time.sleep(1)

            sex = browser.find_element(By.XPATH, '//label[@for="q-7-A8l4-o-1-8l83"]')
            sex.click()

            # time.sleep(1)

            next_btn = browser.find_element(
                By.XPATH, '//button[@class="btn btn-next "]'
            )
            next_btn.click()

            # time.sleep(1)
            #

            degree = browser.find_element(By.XPATH, '//label[@for="q-4-Vqto-o-6-68Dw"]')
            degree.click()

            # time.sleep(1)

            next_btn = browser.find_element(
                By.XPATH, '//button[@class="btn btn-next "]'
            )
            next_btn.click()

            # time.sleep(1)

            #

            family = browser.find_element(
                By.XPATH, '//label[@for="q-11-g2VB-o-0-mC6u"]'
            )
            family.click()

            # time.sleep(1)

            graduate = browser.find_element(
                By.XPATH, '//label[@for="q-12-WBd4-o-0-KyUZ"]'
            )
            graduate.click()

            # time.sleep(1)

            next_btn = browser.find_element(
                By.XPATH, '//button[@class="btn btn-next "]'
            )
            next_btn.click()

            # time.sleep(1000)

            #

            # reason = browser.find_element(By.XPATH, '//label[@for="q-19-AJO6-o-0-4w2k"]')
            # reason.click()

            # time.sleep(1000)

            known = browser.find_element(By.XPATH, '//label[@for="q-19-AJO6-o-0-4w2k"]')
            known.click()

            time.sleep(1)

            submit_btn = browser.find_element(
                By.XPATH, '//button[@class="btn btn-submit "]'
            )
            submit_btn.click()

            time.sleep(2)

    except Exception as e:
        print(e)

    finally:
        browser.quit()


if __name__ == "__main__":
    threads = []
    for i in range(10):
        thread = threading.Thread(target=task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
