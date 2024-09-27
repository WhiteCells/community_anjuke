"""
selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


url = 'http://spfxm.whfgxx.org.cn:8083/spfxmcx/spfcx_index.aspx'

chrome_options = Options()
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(url)
    driver.implicitly_wait(1)

    # 行政选择
    state_select_ele = driver.find_element(By.ID, value='DropDownList_xzq')
    state_select_ele.click()

    # 江夏选项
    jx_option_ele = driver.find_element(By.XPATH, value='//select/option[@value="江夏区"]')
    jx_option_ele.click()

    # 查询按钮
    query_button_ele = driver.find_element(By.XPATH, value='//input[@id="query"]')
    query_button_ele.click()

    def query_one_html():
        # 查找一个页面下的江夏地区小区名
        communities_name_ele = driver.find_elements(By.XPATH, value='//table[@id="tables"]//td/a[@target="_blank"]')
        for community_name in communities_name_ele:
            community_name.click()
            property_table = driver.find_element(By.XPATH, '//a[@onclick="getDengjh()"]')
            property_table.click()
            tables_link = driver.find_elements(By.XPATH, '//tbody[@style="text-align:center;"]//a[@target="_blank"]')
            for tl in tables_link:
                tl.click()
                
                pass
            with open('jx.txt', 'a', encoding='utf8') as f:
                f.write(community_name.text + '\n')

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
