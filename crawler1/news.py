from idlelib.iomenu import encoding

from playwright.sync_api import sync_playwright
from lxml import etree


url = 'https://top.baidu.com/board?platform=pc&sa=pcindex_entry'

# with sync_playwright() as sp:
#     browser = sp.chromium.launch()
#     page = browser.new_page()
#     page.goto(url)
#     html_content = page.content()
#     browser.close()

# print(html_content)

# with open('news.html', 'w', encoding='utf-8') as f:
#     f.write(html_content)

"""
xpath 筛选
"""
with open('news.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# root = etree.fromstring(html_content)
root = etree.HTML(html_content)

# 获取榜单
# ranking_list = root.xpath('//span[@class="title_jDbBV c-theme-color"]/text()')
# for ranking in ranking_list:
#     print(ranking)
#
# # 找每个榜下的内容 + 链接
# titles = root.xpath('//a[@target="_blank"]//div[]')

ranking_title_id = '//span[@class="title_jDbBV c-theme-color"]'
ranking_list = '//div[@class="list_1s-Px"]'

# realtime 模块
realtime_id = '//div[@theme="realtime"]'
# 榜单名
realtime_title = root.xpath(realtime_id + ranking_title_id + '/text()')
print(realtime_title[0])
# 榜单内容



"""
selenium 筛选
"""


