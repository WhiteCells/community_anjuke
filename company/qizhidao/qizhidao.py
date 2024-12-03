import requests
import json
import math
import time
import random
from detail import process_company_detail_page
from hubei_company_db import process_file

url = "https://m.qizhidao.com/api/qzd-bff-mobile/qzd/v1/app/seo/enterprise/directory/queryDirectoryPage"

industry_type_str = """
人工智能 165
证券 146
财务 147
投资 148
保险 145
传媒 174
网络 162
电信 163
建筑 149
工程造价 150
房地产 159
游戏 176
家政 188
回收 191
旅游 195
农业 100
矿业 116
律师 194
影视 178
软件开发 164
物业管理 160
装修 154
煤炭 117
石油化工 118
"""


def industry_type_str_to_map(str):
    industry_type_map = {}
    for line in industry_type_str.splitlines():
        if line == "":
            continue
        kv = line.split()
        if len(kv) == 2:
            industry_type_map[kv[0]] = kv[1]
    return industry_type_map


def create_data(
    current_page: int,
    count_page: int,
    province: str,
    city: str,
    industry_type: str,
    cur_total: int = 0,
):
    data = {
        "current": current_page,
        "pageSize": count_page,
        "address_code_prov": [province],
        "address_code_city": [city],
        "industry_type": industry_type,
        "order": -1,
    }
    json_str = json.dumps(data, separators=(",", ":"))  # `:` `,` 之后不能有空格
    print(json_str)
    print("total:", cur_total)
    return json_str


def create_headers(industry_type: str):
    return {
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9",
        "accesstoken": "eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi45djdXR0JROXdkVlpaaG9XVDFHdVRBLkNhN0RoMThMWmFhaFpkOGp2TWdxU1Z4UVV2UkRaRUttQTVjYXRUcDZERlRzRjZVMHpWanFuN3kzZmh6RWtuZ3BPU1FvLXpOUkl0bmNnazdlVmlzNzZmRG1wSHBwbGJ5RGFNd1hxc0I2NzFxVlFNcWRIb1JLTENEdS14bFVDSEVCeHdFQzFJR3l3Q3JDMXJKbnZlenhDdWc4SUExc19pdEEzNDFud1BGZmhJdmU0b243b2tvcXowUldCeTdlUk93a0tvaHp3Z3N2Z1dwWTZRbzQ2TVZQMG5jZWlTSDJEZVFRVUVtUFp2Qkt5dGMuT1dqcV94aTR4YUNqbHBhV3JIakFVdw.YrUo_lAKGh0xV2nhT-22vuPoScN-sDtsiZpvNStHXGhFtpG_fLj5PhRJwt-uPokz89Od8zCYZNEocMbs_7v62A",
        "content-type": "application/json; charset=UTF-8",
        "cookie": "sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221932d5f54e110c-0b6708379febc6-26011951-2073600-1932d5f54e2851%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzMmQ1ZjU0ZTExMGMtMGI2NzA4Mzc5ZmViYzYtMjYwMTE5NTEtMjA3MzYwMC0xOTMyZDVmNTRlMjg1MSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221932d5f54e110c-0b6708379febc6-26011951-2073600-1932d5f54e2851%22%7D; _bl_uid=wgmvs3qOiqs1yOlj2reOiOgjtv3X; wz_uuid=X%2F3b77a71b852b2e4b0804f182f75af62d; smidV2=20241115103722997d915228b02774544c66607fde9c9a00c54ee9c43966f30; .thumbcache_de0d870e3139ba2368b2e7ea8f11063c=qLpfWcHJ++DXAnGUlz78v9nzwM/MZyhIZAKnzoFEDaFyk1YcKqd5kPdqPIYJAONae0JknnxI3EXoqFxzE+RqzA%3D%3D; accessToken=eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi45djdXR0JROXdkVlpaaG9XVDFHdVRBLkNhN0RoMThMWmFhaFpkOGp2TWdxU1Z4UVV2UkRaRUttQTVjYXRUcDZERlRzRjZVMHpWanFuN3kzZmh6RWtuZ3BPU1FvLXpOUkl0bmNnazdlVmlzNzZmRG1wSHBwbGJ5RGFNd1hxc0I2NzFxVlFNcWRIb1JLTENEdS14bFVDSEVCeHdFQzFJR3l3Q3JDMXJKbnZlenhDdWc4SUExc19pdEEzNDFud1BGZmhJdmU0b243b2tvcXowUldCeTdlUk93a0tvaHp3Z3N2Z1dwWTZRbzQ2TVZQMG5jZWlTSDJEZVFRVUVtUFp2Qkt5dGMuT1dqcV94aTR4YUNqbHBhV3JIakFVdw.YrUo_lAKGh0xV2nhT-22vuPoScN-sDtsiZpvNStHXGhFtpG_fLj5PhRJwt-uPokz89Od8zCYZNEocMbs_7v62A; ips_accessToken=eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi45djdXR0JROXdkVlpaaG9XVDFHdVRBLkNhN0RoMThMWmFhaFpkOGp2TWdxU1Z4UVV2UkRaRUttQTVjYXRUcDZERlRzRjZVMHpWanFuN3kzZmh6RWtuZ3BPU1FvLXpOUkl0bmNnazdlVmlzNzZmRG1wSHBwbGJ5RGFNd1hxc0I2NzFxVlFNcWRIb1JLTENEdS14bFVDSEVCeHdFQzFJR3l3Q3JDMXJKbnZlenhDdWc4SUExc19pdEEzNDFud1BGZmhJdmU0b243b2tvcXowUldCeTdlUk93a0tvaHp3Z3N2Z1dwWTZRbzQ2TVZQMG5jZWlTSDJEZVFRVUVtUFp2Qkt5dGMuT1dqcV94aTR4YUNqbHBhV3JIakFVdw.YrUo_lAKGh0xV2nhT-22vuPoScN-sDtsiZpvNStHXGhFtpG_fLj5PhRJwt-uPokz89Od8zCYZNEocMbs_7v62A; param_sign=dgqHvL; ips_param_sign=dgqHvL; acw_tc=784e2ca517316398949833431e49f60239cabec71e286ca95a2bd29a2b0ff6",
        "origin": "https://m.qizhidao.com",
        "priority": "u=1, i",
        "referer": f"https://m.qizhidao.com/qiye/roster/{industry_type}-000001.html",
        "sec-ch-ua": 'Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "signature": "9772299196835a1d95427184d72e3470.Tn3st3",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "user-agent-web": "X/3b77a71b852b2e4b0804f182f75af62d",
    }


def get_total(rsp):
    try:
        json_data = rsp.json()
        return json_data["data"]["total"]
    except Exception as e:
        print("Exception:", e)
        return None


def parse_rsp(rsp, cur_page, cur_industry_code):
    json_data = rsp.json()
    records = json_data["data"]["records"]
    with open("./company/id_num_industry.txt", "a", encoding="utf-8") as f:
        for r in records:
            id = r["id"]
            name = r["name"]
            reg_address = r["reg_address"]

            if id in id_set:
                print("[continue]", name)
                continue

            detail = process_company_detail_page(id)
            save_data(name, reg_address, detail)

            f.write(id + ":" + str(cur_page) + ":" + cur_industry_code + "\n")
            id_set.add(id)

            print(">>>", name)
            time.sleep(random.uniform(3, 5))


def save_data(name, address, detail):
    with open("./company/武汉.txt", "a", encoding="utf-8") as info_f:
        info_f.write("name:" + name + "&" + "address:" + address)
        for key, val in detail:
            info_f.write("&" + key + ":" + val)
        info_f.write("\n")


def process_post_requests(headers, data):
    return requests.post(url, headers=headers, data=data)


if __name__ == "__main__":
    count_page = 30
    industry_type_map = industry_type_str_to_map(industry_type_str)

    with open("./company/id_num_industry.txt", "a", encoding="utf-8") as f:
        pass

    # 记录之前的状态
    id_set = set()
    industry_code_set = set()
    # 终止页数
    break_page = -1
    # 终止行业，也是最后一个行业，需要特殊处理
    break_industry = ""
    with open("./company/id_num_industry.txt", "r", encoding="utf-8") as f:
        for line in f:
            id_num_industry = line.split(":")
            id = id_num_industry[0].strip()
            id_set.add(id)

            break_page = int(id_num_industry[1].strip())

            industry = id_num_industry[2].strip()
            industry_code_set.add(industry)
            break_industry = industry

    # 选择行业
    for _, industry_code in industry_type_map.items():
        # 处理终止行业，终止行业是否处理完
        if industry_code == break_industry:
            # 总量
            headers = create_headers(break_industry)
            data = create_data(1, 1, "", "420100", break_industry)
            break_industry_total = get_total(process_post_requests(headers, data))
            # 已处理
            processed_num = 0
            with open("./company/id_num_industry.txt", "r", encoding="utf-8") as f:
                for line in f:
                    if line.split(":")[2] == break_industry:
                        processed_num += 1
            # 已处理完成
            if processed_num >= break_industry_total:
                print("[continue] last industry processed")
                continue
            # 未处理完成，继续从终止行业的终止页面开始处理
            else:
                break_industry = ""
        else:
            break_industry = ""

        # 这一次请求是为了获取当前分类的总量
        headers = create_headers(industry_code)
        data = create_data(1, 1, "", "420100", industry_code)  # 地区之后再处理
        rsp = process_post_requests(headers, data)
        print(rsp.text)
        cur_total = get_total(rsp)
        print(">>> total:", cur_total)

        # 需要翻页的次数
        page_count = math.ceil(cur_total / count_page)
        cur_page = 0
        while cur_page <= page_count:
            if break_page == -1:
                cur_page += 1
            else:
                cur_page = break_page
                break_page = -1

            if break_industry != "":
                headers = create_headers(break_industry)
                data = create_data(cur_page, count_page, "", "420100", break_industry, cur_total)
                rsp = process_post_requests(headers, data)
                parse_rsp(rsp, cur_page, break_industry)
            else:
                headers = create_headers(industry_code)
                data = create_data(cur_page, count_page, "", "420100", industry_code, cur_total)
                rsp = process_post_requests(headers, data)
                parse_rsp(rsp, cur_page, industry_code)

            time.sleep(random.uniform(3, 5))

    # 入库
    # process_file("./company/武汉.txt")

"""
request post data:
{
    "current": 1, // 当前页数
    "pageSize": 30, // 页面总数
    "address_code_prov": [province], // 省级代码，如有城市代码，则改代码省略
    "address_code_city": [city], // 市级代码
    "industry_type": industry_type, // 行业代码
    "order": -1, // 排序
}
response:
{
    "data": {
        "total": 14797,
        "size": 100,
        "pages": 148,
        "current": 10,
        "records": [
            {
                "eid": "7d296acc-bed3-47b3-b4fe-81cbaf3791a4",
                "id": "28030198f257bf2cabb1533e1271e8a6",
                "name": "申港证券股份有限公司广西分公司",
                "logo_url": "https://wzdata-api.qizhidao.com/bigtools/big/rk/logo/5936ab1a1edae79aa46c1fde33467e05/db6e531b0d6cc66108eadf0750f4634c",
                "oper_name_title": "负责人",
                "oper_name": "刘思思",
                "pid": "ba9ca5dc350631a999c1a71e961385f6",
                "pid_new": "",
                "status": "存续",
                "reg_address": "南宁市青秀区东葛路118号南宁青秀万达广场西二栋2617、2618、2619、2620、2621室",
                "start_date": "2018-04-26",
                "telephones": "07714606339",
                "high_value_word_list": [
                    "证券经纪",
                    "证券承销与保荐",
                    "证券资产管理",
                    "证券"
                ]
            },
"""
