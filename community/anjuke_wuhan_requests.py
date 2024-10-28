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
    "Cookie": "aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ctid=22; sessid=B2A13EF4-E196-4F8D-BCFB-236830FE6830; _ga=GA1.2.1555425064.1729838090; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; obtain_by=2; twe=2; fzq_h=75e0eb5fbd0c39742dcdfdb0e0d39a51_1730077522608_de39cce412a345c6a86a6153898fe198_1899585074; _gid=GA1.2.1342960644.1730077523; ajk_member_id=298079285; os=other; f_user_ticket=JwUCDQRCI0dARlQhRlFRAA8MFgc2CgdGUVFGUCJGUVFQWlBSV1RUVFNaUVJTUlZTV0ZRUUZRIEZRURYQBhEqB0ZRUUZQIkZRUVFaW1NUWlFbVkZRUUZUJ0BSVFBTU1RbVlJW; wmda_uuid=b2c70a4996e89aa846ab66395cd09c56; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; fzq_js_anjuke_ershoufang_pc=d9c888220a76b123447cb2c77d5f793a_1730079289903_23; new_uv=21; _ga_DYBJHZFBX2=GS1.2.1730081573.6.0.1730081573.0.0.0; fzq_js_ershoufang_fangjia_pc=a023d3fe2879e0356adb10d3d8519c60_1730085271426_00; fzq_js_anjuke_xiaoqu_pc=5fc9bb51eb1474176505197d851cb089_1730085765634_23; ajkAuthTicket=TT=425189545abf8728a0c7c926972b9b40&TS=1730085765927&PBODY=ZSRmrekpAU3kdmhVJMW0JdSnRimrM3kkngwd3_0SjaXyhXVln2tXKq-TeBHMDF1lAUREPIbES5p6ADH85RSdm3bsfhJcLdbqFrnXIdA-fenou4i3l2zlEHE26z2199wyYfCMMaJlDP27_wVkeREXCdcHZmWV6Lm8yO-nkG8K53I&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTczMDA4NTc2NjIwMDQwODc4MnxHTHNTK2tUNEgrM25xeFl2a3oxQWZweDAyREVSZ3c3NGVmcU4zc3ZwRzZ3PXwxZjQ4YzRiNjZlZWRhMWI5MTUxYzhlMDNkZGI4ZGQxMF8xNzMwMDg1NzY1ODM1X2Y5MGYwMjA5ODFmMjQ1ZDg5ZTViNDQ0NTEzOTc4ODc1XzE4OTk1ODUwNzR8ODFkZjE0ODEzZWIyNTUyZDc5OThkZGE2OTY4NmViMTBfMTczMDA4NTc2NTg5Nl8yNTQ=",
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

    with open("./processed.txt", "a", encoding="utf-8") as f, open(
        "./links.txt", "a", encoding="utf-8"
    ) as links_f:
        community_list = root.xpath("//div[@class='list-cell']/a")
        for community in community_list:
            url = community.xpath("./@href")[0]
            links_f.write(url + "\n")

            community_name = community.xpath(
                ".//div[contains(@class, 'li-community-title')]/text()"
            )[0]

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
