import os
import re
import time
import requests
from lxml import etree

res_path = "./wuhan_community2"

prices_list = [
    "m1979",
    "m1980",
    "m1981",
    "m1982",
    "m1983",
    "m1984",
    "m1985",
]


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Cookie": "aQQ_ajkguid=1DAEC9B6-FAB4-44DB-96D9-25FCCEEA4804; sessid=FE723776-A2D3-4B97-9D7D-5E483A053A27; ajk-appVersion=; id58=CrIIUGcXR1EVv9sAEAU3Ag==; xxzlclientid=6bb575c7-0d47-4090-a5ae-1729578833601; xxzlxxid=pfmx/kq6UEJvnRYroz/CS/dHtyoeklrVJSVC7Wpzp+3TQV6ZAFr3b922X6S0d8PlaAqo; 58tj_uuid=7e711c17-ee0f-4286-91fc-2eebc00d1c1d; _ga=GA1.2.1370131655.1729838098; als=0; _ga_DYBJHZFBX2=GS1.2.1729838098.1.1.1729839822.0.0.0; isp=true; fzq_h=5cb29a64cfa9a46d765291cabfee7a7c_1730250632426_150afaebd7ab4731b707471cabec6b44_1899585074; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; obtain_by=2; twe=2; ajk_member_id=298079285; new_uv=5; ctid=22; fzq_js_anjuke_xiaoqu_pc=89916cab400c71f70490506ff0080eb5_1730275746539_24; ajkAuthTicket=TT=7dba56593d84880affde6e233a79d928&TS=1730275746947&PBODY=aJ2Ci5bUYZBCqFt2VHOckOaW6kCU7F2a7oY_uZ2Nd045XZc9D5fvg1tqAv6Y_-veiDMx1RUww31mledinzM47FQQvOavtRJghVhKIPx2U9G2hXENzqj3qDDPo29R3X5KQREV8OAaSjtPm4g1EGy0RnyrkcoZwslJVmoHI26M3qE&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTczMDI3NTc0NzI3MjIxODI0MnxBRHZLbkpaa3gwSW9paGpQQ0dkSnRkbkhvcUIvbjFoNmVoQVVnRmcvRGpJPXxiMGI4ZGI4MjY2NGY3ZGE0MjQ5MmEyYjgxYjQ2ZWZhMF8xNzMwMjc1NzQ2Nzg3X2YwZWQwYzM3MWYwMDQ2MTY5NDcwYmY1MmQwNjM2NDgxXzE4OTk1ODUwNzR8ZWEzY2NmNWM0N2Q1MmE3NjhjZTY2Nzg3YWNiM2NmOTZfMTczMDI3NTc0Njg5OF8yNTU=",
}


def get_region_name(url):
    return url.split("/")[-2]


def get_num_page_url(url, num):
    return url.rstrip("/") + f"-p{num}"


def get_cur_community_num(str):
    return int(re.search(r"\d+", str).group())


def get_community_id(url):
    return url.split("/")[-1]


def process_detail_page(url, community_name, i):
    """
    处理详细页面
    """
    rsp = requests.get(url, headers=headers)
    print(rsp.text)
    with open(f"{res_path}/{i}_{community_name}.html", "w", encoding="utf-8") as f:
        f.write(rsp.text)


def process_one_page(url, i):
    rsp = requests.get(url, headers=headers)
    root = etree.HTML(rsp.text)

    community_id_set = set()
    with open("./processed.txt", "r", encoding="utf-8") as f:
        for line in f:
            community_id_set.add(line.strip())

    with open("./processed.txt", "a", encoding="utf-8") as f, open("./links.txt", "a", encoding="utf-8") as links_f:
        community_list = root.xpath("//div[@class='list-cell']/a")
        for community in community_list:
            url = community.xpath("./@href")[0]
            links_f.write(url + "\n")

            community_name = community.xpath(".//div[contains(@class, 'li-community-title')]/text()")[0]

            community_id = get_community_id(url)
            if community_id in community_id_set:
                continue
            f.write(community_id + "\n")

            print(url)
            print(community_name)

            time.sleep(1)
            process_detail_page(url, community_name, i)


def process_list_page(url):
    rsp = requests.get(url, headers=headers)

    root = etree.HTML(rsp.text)
    try:
        # 获取当前分类的小区个数
        cur_community_num_str = root.xpath("//span[@class='total-info']/text()")[0]
        cur_community_num = get_cur_community_num(cur_community_num_str)
        # 在选择地区和价格后需要访问的页数
        page_cnt = cur_community_num // 25 + 1
        for i in range(1, page_cnt + 1):
            page_url = get_num_page_url(url, i)
            print(page_url)
            time.sleep(1)
            process_one_page(page_url, i)
    except Exception as e:
        print("Exception: ", e)


def select_region_and_price(region_link_list):
    one_row = True
    for region_link in region_link_list:
        if one_row:
            one_row = False
            continue

        for price in prices_list:
            rp_link = region_link + price
            print(rp_link)

            time.sleep(1)
            process_list_page(rp_link)


def enter_communiy_page():
    url = "https://wuhan.anjuke.com/community/"
    rsp = requests.get(url, headers=headers)

    root = etree.HTML(rsp.text)
    region_link_list = root.xpath("//li[@class='region-item']/a/@href")

    for region_link in region_link_list:
        print(region_link)

    select_region_and_price(region_link_list)


if __name__ == "__main__":
    print(os.getcwd())
    if not os.path.exists(res_path):
        os.mkdir(res_path)
    enter_communiy_page()
