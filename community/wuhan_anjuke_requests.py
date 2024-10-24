import os
import time
import requests
from lxml import etree


res_path = "./wuhan_community"


def process_detail_page(url, name):
    """
    处理详细页面
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Cookie": "",
    }
    rsp = requests.get(url, headers=headers)
    with open(res_path + "/" + name + ".html", "w", encoding="utf-8") as f:
        f.write(rsp.text)


def process_list_page(url):
    """
    处理列表页面
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Cookie": "",
    }
    rsp = requests.get(url, headers=headers)
    print(rsp.text)

    root = etree.HTML(rsp.text)

    community_list = root.xpath("//div[@class='list-cell']")

    for community in community_list:
        url = community.xpath("./a/@href")[0]
        name = community.xpath(
            "./a//div[@class='nowrap-min li-community-title']/text()"
        )[0]
        process_detail_page(url, name)
        time.sleep(1)


def select_region_and_price(url):
    """
    选择地区和价格
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; twe=2; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; fzq_h=dff59bdf0e571eac870107de44dd8df5_1729732062486_1c9b564d8baf41f38c8316b50d0d75b6_1899585074; ctid=22; new_uv=6; obtain_by=2; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729757328540&PBODY=SqCjHJoMVq3p3_6HpXYU3yXjI2af4FrpbMHVwco8pN8FPxnwu9hfxlhLJjYJSTYCreQCls75oPm5yltybUN2Ko-3M9JKxN8tYiL8onhMOSWY0fg6qBx2vxwWhjcFWhZiWd71J5eGGZbzwNlRyHSu8gvn5LwdIP8srGCvf96Yimk&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; fzq_js_anjuke_xiaoqu_pc=f1e93b9a4342f49c741c4d813cb0a2e5_1729757329843_24; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTcyOTc1NzMzMTIwMjkzNTE4MXxVWitKWkxnbjlUT1RZVEc0YVlteWZ3aDNkVy80NkZ2S05VZzdNK1dRLy9JPXwyZTdhNDA1NzFkMWZlMWY1M2RkNWRhOTVjNGQ4NmJlZV8xNzI5NzU3MzMwMTY3X2ZkYzY0NWVjNzBhODQxMTM4MTFiZThkYjNlOTRhMTEzXzE4OTk1ODUwNzR8M2JmNzY5NTc0ZGMwMDhmZWFlYmIwMWE2YmFhYzkxYTJfMTcyOTc1NzMzMDM2Nl8yNTQ=",
    }
    rsp = requests.get(url, headers=headers)
    print(rsp.text)
    with open("region.html", "w", encoding="utf-8") as f:
        f.write(rsp.text)

    root = etree.HTML(rsp.text)
    region_link_list = root.xpath("//li[@class='region-item']/a/@href")

    for region_link in region_link_list:
        headers2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; twe=2; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; fzq_h=dff59bdf0e571eac870107de44dd8df5_1729732062486_1c9b564d8baf41f38c8316b50d0d75b6_1899585074; ctid=22; obtain_by=2; new_uv=7; fzq_js_anjuke_xiaoqu_pc=6b9a303b3229719b4f784a96c3dab295_1729764041885_23; ajkAuthTicket=TT=425189545abf8728a0c7c926972b9b40&TS=1729764042559&PBODY=od8hIrsaHmnXHkm8X8B98KidxzqbgEmiCNQpiWwz0QMFMJoIZakd1N6W2G44vCaL01zCkxCarLr0MnoP7JsflI0gjYReMDOn7uPqvE6G7Vr0KRUsaoQQGb30a3ONj6voSXa6WFuyaG4vA1p6BbrHvLq7F4qtR6vLHmiqdLWo3Gg&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTcyOTc2NDA0MzEzMjU0MTE4MXxYcXNmeUVaOXc1SVhSVmx6ZnpWUkJCQWlwUUFXWFpVL0pwSlV5QlRuRE9BPXw5NGIwZWFiYmY5Yjc2MTYxYTA1MTM0MTAxOThhODIyZV8xNzI5NzY0MDQyMzk0X2QzYTc2MzhiYmE1YzRjNGU4NTUzMDlmYTdiM2YzYTRiXzE4OTk1ODUwNzR8YmFlZDQ2ZmRhZmZhMjZlNDkzODEzMzQwODBkNGEzZTJfMTcyOTc2NDA0MjUxNV8yNTQ=",
        }
        region_rsp = requests.get(region_link, headers=headers2)
        region_root = etree.HTML(region_rsp.text)
        price_link_list = region_root.xpath("//li[@class='price-item']/a/@href")
        for price_link in price_link_list:
            process_list_page(price_link)
            time.sleep(1)


def enter_communiy_page():
    url = "https://wuhan.anjuke.com/community/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; twe=2; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; fzq_h=dff59bdf0e571eac870107de44dd8df5_1729732062486_1c9b564d8baf41f38c8316b50d0d75b6_1899585074; ctid=22; obtain_by=2; new_uv=7; fzq_js_anjuke_xiaoqu_pc=c647014fa5066b7307b5c66d5a4bfcaa_1729760873803_25; ajkAuthTicket=TT=425189545abf8728a0c7c926972b9b40&TS=1729760874598&PBODY=N3v-9oM5227ETglymSA3cPBb7YF_38fgWqDb8J8Z7_PPzENzCEmJkSZRYyJOU-yKgxnEHGTfW6oe8UvKjhzoqiX02T6baZVDf822SEEcffwr5qkMFowgCye4VqqYFzu7eAlsKRAmIU6H-1tCYL3txQlYebP_ZTCHt5wFBNPsd7A&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTcyOTc2MDg3NDU4NDYzMjgyNnxlVzJ5cEk4d01GYnBqc0luTkRoSEJXak9XWGJjWHg4cEZ2L3UybXFweWg0PXwwZmJmYjEyMjIzNjBkNDQxNzg1MzM3Njk1YjQ2MTZhOF8xNzI5NzYwODc0MTE2XzBiNmZmN2JhOGRlMTQ5ODViMWM0ZTc3Y2E2MjU3YWUyXzE4OTk1ODUwNzR8ZDg0YWEzY2E3MjgxY2I1ZWZkMjY3YWM0MTM1ZWQ2ZWNfMTcyOTc2MDg3NDE1Ml8yNTY=",
    }
    rsp = requests.get(url, headers=headers)
    print(rsp.text)
    with open("community.html", "w", encoding="utf-8") as f:
        f.write(rsp.text)

    root = etree.HTML(rsp.text)
    region_link_list = root.xpath("//li[@class='region-item']/a/@href")

    for region_link in region_link_list:
        select_region_and_price(region_link)
        time.sleep(1)


if __name__ == "__main__":
    if not os.path.exists(res_path):
        os.mkdir(res_path)
    enter_communiy_page()
