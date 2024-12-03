from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import re

from thread_pool import ThreadPool

url = "http://spfxm.whfgxx.org.cn:8083/spfxmcx/spfcx_index.aspx"
# proxy = "101.43.8.71:3128"
# proxy = "124.223.78.216:3128"

chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument(f"--proxy-server={proxy}")

driver = webdriver.Chrome(options=chrome_options)

community_path = "./whfgxx_community"


def clean_name(name):
    """
    清除名称中特殊的字符
    """
    return re.sub(r'[<>:"/\\|?*]', "", name)


def task(district: str):
    try:
        # 行政选择
        driver.find_element(By.ID, value="DropDownList_xzq").click()

        # 区选项
        driver.find_element(By.XPATH, value=f'//select/option[@value="{district}"]').click()

        # 查询按钮
        driver.find_element(By.XPATH, value='//input[@id="query"]').click()

        main_window = driver.current_window_handle

        def query_one_html():
            # main_window = driver.current_window_handle

            communities_ele = driver.find_elements(By.XPATH, '//table[@id="tables"]//td/a[@target="_blank"]')

            for community in communities_ele:
                community_str = clean_name(community.text)
                print("===> ", community_str)
                one_community_path = f"{community_path}/{community_str}"
                if not os.path.exists(one_community_path):
                    os.makedirs(one_community_path)

                community.click()

                # 切换到小区详细页面
                driver.switch_to.window(driver.window_handles[-1])
                print("[title]: ", driver.title)
                table_link = driver.find_element(By.XPATH, '//table[@id="table_mx"]//a[@id="href1"]')
                print("---> ", table_link.text)
                table_link.click()

                driver.switch_to.window(driver.window_handles[-1])
                buildings = driver.find_elements(By.XPATH, '//tbody[@style="text-align:center;"]//td/a[@target="_blank"]')

                building_window = driver.current_window_handle
                for building in buildings:
                    building_str = clean_name(building.text)

                    print("[building name]", building_str)
                    # 点击栋名
                    building.click()
                    # 切换到栋的页面
                    print("build title: ", driver.current_window_handle.title)
                    driver.switch_to.window(driver.window_handles[-1])
                    details = driver.find_elements(By.XPATH, '//table[@class="tab_style"]//tr')

                    for detail in details:
                        print(detail.text)
                        with open(f"{one_community_path}/{building_str}.txt", "a", encoding="utf-8") as f:
                            f.write(detail.text + "\n")

                    driver.close()
                    driver.switch_to.window(building_window)

                # 切换回小区名列表
                driver.switch_to.window(main_window)

        def click_next_page(x: int):
            next_page_ele_attribute = f"//a[@href=\"javascript:__doPostBack('AspNetPager1','{x}')\"]"
            print(next_page_ele_attribute)
            next_page_ele = driver.find_element(By.XPATH, value=next_page_ele_attribute)
            next_page_ele.click()

        # 总页数
        page_count_ele = driver.find_element(By.XPATH, value='//div[@class="pages"]/font')
        if not page_count_ele:
            query_one_html()
            return
        print(page_count_ele.text)
        page_count = int(page_count_ele.text)
        print(page_count)

        for i in range(2, page_count + 2):
            query_one_html()
            driver.switch_to.window(main_window)
            # 最后一页不翻页
            if i - 1 < page_count:
                click_next_page(i)

    finally:
        driver.quit()


if __name__ == "__main__":
    driver.get(url)
    driver.implicitly_wait(1)
    district_ele_list = driver.find_elements(By.XPATH, "//select/option")
    for district_ele in district_ele_list:
        print(district_ele.text)
