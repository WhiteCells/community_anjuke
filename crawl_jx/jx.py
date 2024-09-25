# import requests
#
#
# payload = {
#     '': ''
# }
#
# headers = {
#     'user-agent:': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
# }
#
# response = requests.post('http://spfxm.whfgxx.org.cn:8083/spfxmcx/spfcx_index.aspx', headers=headers, data=payload)
#
# print(response.text)

"""
playwright
xpath
"""
# from playwright.sync_api import sync_playwright
# from lxml import etree
#
#
# url = 'http://spfxm.whfgxx.org.cn:8083/spfxmcx/spfcx_index.aspx'
#
# def get_html_content():
#     with sync_playwright() as sp:
#         browser = sp.chromium.launch()
#         page = browser.new_page()
#         page.goto(url)
#         html_content = page.content()
#         browser.close()
#     return html_content
#
# html_content = get_html_content()
#
# with open('jx.html', 'w', encoding='utf-8') as f:
#     f.write(html_content)
#
# root = etree.HTML(html_content)
#
# communities_name = root.xpath('//div[@class="tabs"]//tr/td/a/text()')
#
# for community in communities_name:
#     print(community)

"""
selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


url = 'http://spfxm.whfgxx.org.cn:8083/spfxmcx/spfcx_index.aspx'

driver = webdriver.Chrome()

try:
    driver.get(url)
    driver.implicitly_wait(1)

    # 行政选择
    state_select_ele = driver.find_element(By.ID, value='DropDownList_xzq')
    state_select_ele.click()
    # time.sleep(5)

    # 江夏选项
    jx_option_ele = driver.find_element(By.XPATH, value='//select/option[@value="江夏区"]')
    jx_option_ele.click()
    # time.sleep(5)

    # 查询按钮
    query_button_ele = driver.find_element(By.XPATH, value='//input[@id="query"]')
    query_button_ele.click()
    # time.sleep(5)

    def query_one_html():
        # 查找一个页面下的江夏地区小区名
        communities_name_ele = driver.find_elements(By.XPATH, value='//table[@id="tables"]//td/a[@target="_blank"]')
        for community_name in communities_name_ele:
            print(community_name.text)
        # return communities_name

    def click_next_page(x: int):
        next_page_ele_attribute = f'//a[@href="javascript:__doPostBack(\'AspNetPager1\',\'{x}\')"]'
        print(next_page_ele_attribute)
        next_page_ele = driver.find_element(By.XPATH, value=next_page_ele_attribute)
        next_page_ele.click()

    # 总页数
    page_count_ele = driver.find_element(By.XPATH, value='//div[@class="pages"]/font')
    page_count = int(page_count_ele.text)
    print(page_count)

    for i in range(2, page_count + 2):
        query_one_html()
        # 最后一页不翻页
        if i - 1 < page_count:
            click_next_page(i)

finally:
    driver.quit()
