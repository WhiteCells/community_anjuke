import requests
import time
from lxml import etree
from community.anjuke_wuhan_requests import process_detail_page

url = "https://wuhan.anjuke.com/sale/rd1/?q="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Cookie": "aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ctid=22; sessid=B2A13EF4-E196-4F8D-BCFB-236830FE6830; _ga=GA1.2.1555425064.1729838090; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; twe=2; fzq_h=75e0eb5fbd0c39742dcdfdb0e0d39a51_1730077522608_de39cce412a345c6a86a6153898fe198_1899585074; _gid=GA1.2.1342960644.1730077523; ajk_member_id=298079285; os=other; f_user_ticket=JwUCDQRCI0dARlQhRlFRAA8MFgc2CgdGUVFGUCJGUVFQWlBSV1RUVFNaUVJTUlZTV0ZRUUZRIEZRURYQBhEqB0ZRUUZQIkZRUVFaW1NUWlFbVkZRUUZUJ0BSVFBTU1RbVlJW; wmda_uuid=b2c70a4996e89aa846ab66395cd09c56; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; fzq_js_ershoufang_fangjia_pc=a023d3fe2879e0356adb10d3d8519c60_1730085271426_00; new_uv=23; _ga_DYBJHZFBX2=GS1.2.1730093718.8.0.1730093718.0.0.0; fzq_js_anjuke_xiaoqu_pc=c784aa175f290e13ea510756bb2dad68_1730100316120_25; fzq_js_anjuke_ershoufang_pc=a1f2e8c8b60f788482ec4374de9d2114_1730102285345_25; obtain_by=1; ajkAuthTicket=TT=425189545abf8728a0c7c926972b9b40&TS=1730102285723&PBODY=YaKE_2esoizVfg2NPJwEKvf408lUwdxxYOPG7jrhcs-851o3tpoul8R96tvS9gklZWbHS8oHeuhBHba6m0eNHYz0aW62wTKtDg2cArJAuNF8Ihail39rfy8uOkG3C_rLKbr5FAjLwpv7gdUMsovaZXZWLkMlNtadgEhyjpHkGWU&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTczMDEwMjI4NjcwMjI2NDI3NXxZNG94UnQvSlRGSnRyd1EyeEx3a2xtY2tWZU0wYzBZR2FiaFl1eWE4TGVjPXwxM2Y1ODJjZmZiODE4YmZkYjkyZDNmOWU1MjljYmQ2N18xNzMwMTAyMjg1NTI3XzdkNzBjNGQyOWEwMjQ2YTNhMTM4Y2YyODljNjU4YTBjXzE4OTk1ODUwNzR8OWZjOTkwYzRjMmQzYTZlMzQzZTY5NjZjOWJmYTljNWVfMTczMDEwMjI4NTkxNl8yNTQ=",
}

with open("delete_list.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        name = line.split(".")[0].split("_")[1]
        print(name)
        new_url = url + name
        rsp = requests.get(new_url, headers=headers)
        root = etree.HTML(rsp.text)
        # print(rsp.text)
        link = root.xpath("//div[@class='community-table']/a/@href")[0]
        print(link)
        time.sleep(1)
        process_detail_page(link, name, 0)
