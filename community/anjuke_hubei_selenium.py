import time
import os
import cv2
import requests
import random
import re
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# from db import HubeiCommunity, add_community, Base, engine

res_path = "./hubei/"

url = "https://www.anjuke.com/sy-city.html"

chrome_options = Options()
chrome_options.debugger_address = "127.0.0.1:9222"

verify_block_out_path = "./verify_block_img"

"""
101.43.8.71:3128
start chrome.exe --remote-debugging-port=9222,--proxy-server=101.43.8.71:3128
124.223.78.216:3128
start chrome.exe --remote-debugging-port=9222,--proxy-server=124.223.78.216:3128
"""


def get_region_name(url):
    return url.split("/")[-2]


def get_num_page_url(url, num):
    return url.rstrip("/") + f"-p{num}"


def get_cur_community_num(str):
    return int(re.search(r"\d+", str).group())


def get_community_id(url):
    return url.split("/")[-1]


def is_age_route(text):
    pattern = r"(\d+(\.\d+)?年|\d+-\d+年)"
    return re.findall(pattern, text)


def save_verify_block(driver: webdriver.Chrome):
    """
    保存验证图片
    """
    bg_img_ele = driver.find_element(By.XPATH, "//img[@class='dvc-captcha__bgImg']")
    bg_img_href = bg_img_ele.get_attribute("src")
    print("bg_img_href: ", bg_img_href)

    target_img_ele = driver.find_element(By.XPATH, "//img[@class='dvc-captcha__puzzleImg']")
    target_img_href = target_img_ele.get_attribute("src")
    print("target_img_href: ", target_img_href)

    bg_img_rsp = requests.get(bg_img_href)
    with open(f"{verify_block_out_path}/bg.png", "wb") as f:
        f.write(bg_img_rsp.content)

    target_img_rsp = requests.get(target_img_href)
    with open(f"{verify_block_out_path}/target.png", "wb") as f:
        f.write(target_img_rsp.content)


def process_verify_block() -> int:
    """
    处理验证图片，返回滑验证图片需要移动的偏移量
    """

    def white_mask_img(image):
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # 定义更精确的白色的HSV范围
        lower_white = np.array([0, 0, 220])  # 提高最低亮度
        upper_white = np.array([180, 30, 255])  # 降低饱和度上限

        # 生成白色区域的掩码
        white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

        # 保留彩色信息，仅显示白色区域
        white_part_color = cv2.bitwise_and(image, image, mask=white_mask)
        cv2.imwrite(f"{verify_block_out_path}/res2.png", white_part_color)
        return white_part_color

    try:
        # 读取并处理背景和目标图像
        bg = cv2.imread(f"{verify_block_out_path}/bg.png")
        target = cv2.imread(f"{verify_block_out_path}/target.png")
        bg = white_mask_img(bg)
        target = white_mask_img(target)

        # 边缘检测，优化参数
        bg_canny = cv2.Canny(bg, 50, 150)  # 改为更低的阈值范围
        target_canny = cv2.Canny(target, 50, 150)

        # 进行模板匹配
        res = cv2.matchTemplate(bg_canny, target_canny, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        print("max_val: ", max_val)

        height, width = target_canny.shape[:2]
        x1, y1 = max_loc[0], max_loc[1]
        x2, y2 = x1 + width, y1 + height

        # 可视化匹配结果
        cv2.rectangle(bg, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.imwrite(f"{verify_block_out_path}/res.png", bg)

        # 更精确地计算需要滑动的距离
        element_width = 280  # HTML 元素宽度
        actual_image_width = 480  # 图片实际宽度
        offset_x = element_width * (x1 / actual_image_width)

        print("计算的偏移量:", offset_x)
        return int(round(offset_x))

    except Exception as e:
        print(">>> process_verify_block Exception:", e)


def mv_verify_block(driver: webdriver.Chrome, offset: int):
    """
    移动验证图片
    """
    try:
        slider_handler = driver.find_element(By.XPATH, "//div[@class='dvc-slider__handler']")
        ActionChains(driver).click_and_hold(slider_handler).pause(0.5).perform()
        ActionChains(driver).move_by_offset(xoffset=offset, yoffset=0).pause(0.8).perform()
        ActionChains(driver).release().pause(0.9).perform()
        time.sleep(random.uniform(2, 4))
    except Exception as e:
        print(">>> mv_verify_block Exception:", e)


def random_sleep_time():
    time.sleep(random.uniform(4, 5))


def task(city: str):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    print(driver.title)
    random_sleep_time()

    def enter_communiy_page(url):
        """
        传入城市的 url
        """
        driver.get(url)
        random_sleep_time()

        if "访问验证" in driver.title:
            print("访问验证")
            input("Press any key to continue...")

        region_link_list = []
        region_link_ele_list = driver.find_elements(By.XPATH, "//li[@class='region-item']/a")
        one_row = True
        for region_link_ele in region_link_ele_list:
            if one_row:
                one_row = False
                continue
            region_url = region_link_ele.get_attribute("href")
            print(region_url)
            region_link_list.append(region_url)

        price_route_list = []
        price_route_ele_list = driver.find_elements(By.XPATH, "//li[@class='line-item']/a")
        for link in price_route_ele_list:
            href = link.get_attribute("href")
            text = link.text
            if is_age_route(text):
                continue
            if href.split("/")[-2] == "community":
                continue
            print(href)
            route = href.split("/")[-2]
            print(route)
            price_route_list.append(route)

        select_region_and_age(region_link_list, price_route_list)

    def select_region_and_age(region_link_list, price_route_list):
        """
        构建 `区` 和 `房龄` 的链接
        """
        for region_link in region_link_list:
            for price in price_route_list:
                ra_link = region_link + price
                print(f"create url {ra_link}")
                random_sleep_time()

                process_list_page(ra_link)

    def process_list_page(url):
        """
        计算分页的页数，并访问
        """
        print(f"\n>>> process_list_page: {url}")
        driver.get(url)
        random_sleep_time()

        try:
            # 获取当前分类的小区个数（可能异常）
            cur_community_num_str = driver.find_element(By.XPATH, "//span[@class='total-info']").text
            if not cur_community_num_str:
                print("[Warning] cur_community_num_str not found, skiping page")
                return
            cur_community_num = get_cur_community_num(cur_community_num_str)
            # 在选择地区和价格后需要访问的页数
            # page_cnt = cur_community_num // 25 + 1
            page_cnt = cur_community_num // 25 if cur_community_num % 25 == 0 else cur_community_num // 25 + 1
            print("page_cnt:", page_cnt)
            for i in range(1, page_cnt + 1):
                page_url = get_num_page_url(url, i)
                random_sleep_time()
                process_one_page(page_url)

        except Exception as e:
            # 可能无小区
            print(f"[Exception] process_list_page: {e}")

    def process_one_page(url):
        """
        直接从单页中获取 `名称` `地址`
        """
        print(f"\n>>> process_one_page: {url}")
        driver.get(url)
        random_sleep_time()

        if "访问验证" in driver.title:
            print("访问验证")
            input("Press any key to continue...")

        if not os.path.exists(f"./{res_path}"):
            os.mkdir(f"./{res_path}")

        if not os.path.exists(f"./{res_path}/processed.txt"):
            with open(f"./{res_path}/processed.txt", "w", encoding="utf-8") as f:
                pass

        community_id_set = set()
        with open(f"./{res_path}/processed.txt", "r", encoding="utf-8") as f:
            for line in f:
                community_id_set.add(line.strip())

        with open(f"./{res_path}/processed.txt", "a", encoding="utf-8") as f:
            community_list = driver.find_elements(By.XPATH, "//div[@class='list-cell']/a")
            if not community_list:
                print("[Warning] No communities found on this page.")
                return
            for community in community_list:
                url = community.get_attribute("href")
                community_id = get_community_id(url)
                community_name = community.find_element(By.XPATH, ".//div[@class='nowrap-min li-community-title']").text

                # community_address = community.find_elements(By.XPATH, ".//div[@class='props nowrap']/span")[1].text
                community_address_spans = community.find_elements(By.XPATH, ".//div[@class='props nowrap']/span")
                if len(community_address_spans) > 2:
                    community_address = community_address_spans[2].text
                else:
                    community_address = community_address_spans[0].text
                district = community_address.split("-")[0].strip()
                if community_id in community_id_set:
                    print(f"---> {community_name} - {community_id} existed")
                    continue

                f.write(community_id + "\n")

                print(f"小区id: {community_id}")
                print(f"城市: {city}")
                print(f"小区名: {community_name}")
                print(f"小区地址: {community_address}")

                # add_community(HubeiCommunity, community_name, city, district, community_address)
                with open(f"{res_path}/res.txt", "a", encoding="utf-8") as res_f:
                    res_f.write(community_id + "/" + community_name + "/" + city + "/" + district + "/" + community_address + "\n")

    ####################################

    # 查找 city
    city_ele = driver.find_element(By.XPATH, f"//ul[@class='ajk-city-cell-content']//a[text()='{city}']")
    city_ele.click()
    random_sleep_time()

    # 查看更多
    more_ele = driver.find_element(By.XPATH, "//div[@class='recommend-title']/a")
    more_href = more_ele.get_attribute("href")

    enter_communiy_page(more_href)

    random_sleep_time()

    driver.quit()


if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    if not os.path.exists(res_path):
        os.mkdir(res_path)
    if not os.path.exists(verify_block_out_path):
        os.mkdir(verify_block_out_path)

    city_list = [
        "武汉",
        "黄石",
        "十堰",
        "宜昌",
        "襄阳",
        "鄂州",
        "荆门",
        "孝感",
        "荆州",
        "黄冈",
        "咸宁",
        "随州",
        "仙桃",
        "天门",
        "潜江",
    ]
    for city in city_list:
        task(city)
