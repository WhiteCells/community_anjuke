import requests
from lxml import etree

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; _bl_uid=wgmvs3qOiqs1yOlj2reOiOgjtv3X; wz_uuid=X%2F3b77a71b852b2e4b0804f182f75af62d; smidV2=20241115103722997d915228b02774544c66607fde9c9a00c54ee9c43966f30; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221932d5f54e110c-0b6708379febc6-26011951-2073600-1932d5f54e2851%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzMmQ1ZjU0ZTExMGMtMGI2NzA4Mzc5ZmViYzYtMjYwMTE5NTEtMjA3MzYwMC0xOTMyZDVmNTRlMjg1MSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221932d5f54e110c-0b6708379febc6-26011951-2073600-1932d5f54e2851%22%7D; Hm_lvt_81eccb3e41e82aaede63da695f20adf2=1731923174; acw_tc=784e2c9417319782345082540e1576baeb03732981fb884d17f26bb68c9d75; .thumbcache_de0d870e3139ba2368b2e7ea8f11063c=NdIF8IvpOkGQC4keJ758K1QHR1APUNzGqPcujq4iwZsk7wS767qGa9lQsNTmQPMIbvzhEQUHOzr9BtooaTio7g%3D%3D",
    "priority": "u=0, i",
    "referer": "https://m.qizhidao.com/qiye/roster/165-000001.html",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}


def process_company_detail_page(id: str) -> tuple:
    """
    处理详细页面

    :param id: 公司id
    """
    # + (id)"6f904d6f932c2f38d7219abfe0796c69" + ".html"
    url = "https://m.qizhidao.com/qiye/company/" + id + ".html"
    rsp = requests.get(url, headers=headers)

    root = etree.HTML(rsp.text)

    # 3 个，个别需要要特殊处理，不使用循环
    attrlist_divs = root.xpath("//div[@class='attrlist']")

    # [0]
    part1 = attrlist_divs[0]

    # 法定代表人
    legal_person_texts = part1.xpath("//a[@class='info blue-info']/text()")[0]
    # print("法定代表人", legal_person_texts)

    divs = part1.xpath("./div")

    # 成立时间
    founded_span = divs[1].xpath("./div[@class='value']/span[1]/text()")[0]
    # print("成立时间:", founded_span)

    # 企业经营状态
    business_status_text = divs[2].xpath("./div[@class='value']/span[1]/text()")[0]
    # print("企业经营状态:", business_status_text)

    # 注册资本
    register_capital_text = divs[3].xpath("./div[@class='value']/span[1]/text()")[0]
    # print("注册资本:", register_capital_text)

    # 实缴资本
    paid_capital_text = divs[4].xpath("./div[@class='value']/span[1]/text()")[0]
    # print("实缴资本:", paid_capital_text)

    # 企业类型
    business_type_text = divs[5].xpath("./div[@class='value']/span[1]/text()")[0]
    # print("企业类型:", business_type_text)

    # 所属行业
    business_industry_text = divs[6].xpath("./div[@class='value']/span[1]/text()")[0]
    # print("所属行业:", business_industry_text)

    # [1]
    part2 = attrlist_divs[1]
    # 统一社会信用代码
    credit_code_text = part2.xpath("./div[1]/div[@class='value']/span[1]/text()")[0]
    # print("统一社会信用代码:", credit_code_text)

    # 工商注册号
    register_code_text = part2.xpath("./div[2]/div[@class='value']/span[1]/text()")[0]
    # print("工商注册号:", register_code_text)

    # 组织机构类型
    org_type_text = part2.xpath("./div[3]/div[@class='value']/span[1]/text()")[0]
    # print("组织机构类型:", org_type_text)

    # 组织结构代码
    org_code_text = part2.xpath("./div[4]/div[@class='value']/span[1]/text()")[0]
    # print("组织结构代码:", org_code_text)

    # 参保人数
    insured_num_text = part2.xpath("./div[5]/div[@class='value']/span[1]/text()")[0]
    # print("参保人数:", insured_num_text)

    # 员工人数
    employee_num_text = part2.xpath("./div[6]/div[@class='value']/span[1]/text()")[0]
    # print("员工人数:", employee_num_text)

    # 纳税人识别号
    taxpayer_code_text = part2.xpath("./div[7]/div[@class='value']/span[1]/text()")[0]
    # print("纳税人识别号", taxpayer_code_text)

    # 纳税人资质
    taxpayer_qualification_text = part2.xpath("./div[8]/div[@class='value']/span[1]/text()")[0]
    # print("纳税人资质", taxpayer_qualification_text)

    # 进出口企业代码
    import_export_code_text = part2.xpath("./div[9]/div[@class='value']/span[1]/text()")[0]
    # print("进出口企业代码", import_export_code_text)

    # 海关注册编码
    sea_code_text = part2.xpath("./div[10]/div[@class='value']/span[1]/text()")[0]
    # print("海关注册编码", sea_code_text)

    # [2]
    part3 = attrlist_divs[2]
    # 经营期限
    business_period_text = part3.xpath(".//div[@class='value']/span[1]/text()")[0]
    # print("经营期限", business_period_text)

    # 核准日期
    approved_date_text = part3.xpath("./div[2]/div[@class='value']/span[1]/text()")[0]
    # print("核准日期", approved_date_text)

    # 登记机关
    register_authority_text = part3.xpath("./div[3]/div[@class='value']/span[1]/text()")[0]
    # print("登记机关", register_authority_text)

    # 曾用名
    used_name_text = part3.xpath("./div[4]/div[@class='value']/span[1]/text()")[0]
    # print("曾用名", used_name_text)

    # 英文名
    eng_name_text = part3.xpath("./div[5]/div[@class='value']/span[1]/text()")[0]
    # print("英文名", eng_name_text)

    # 经营范围
    business_scope_text = part3.xpath("./div[6]//p")[0].text
    # print("经营范围", business_scope_text)

    ## 中断不便处理
    # with open("./company/武汉.txt", "a", encoding="utf-8") as f:
    #     f.write("legal_person:" + legal_person_texts + "&")
    #     f.write("founded_time:" + founded_span + "&")
    #     f.write("business_status:" + business_status_text + "&")
    #     f.write("register_capital:" + register_capital_text + "&")
    #     f.write("paid_capital:" + paid_capital_text + "&")
    #     f.write("business_type:" + business_type_text + "&")
    #     f.write("business_industry:" + business_industry_text + "&")
    #     f.write("credit_code:" + credit_code_text + "&")
    #     f.write("register_code:" + register_code_text + "&")
    #     f.write("org_type:" + org_type_text + "&")
    #     f.write("org_code:" + org_code_text + "&")
    #     f.write("insured_num:" + insured_num_text + "&")
    #     f.write("employee_num:" + employee_num_text + "&")
    #     f.write("taxpayer_code:" + taxpayer_code_text + "&")
    #     f.write("taxpayer_qualification:" + taxpayer_qualification_text + "&")
    #     f.write("import_export_code:" + import_export_code_text + "&")
    #     f.write("sea_code:" + sea_code_text + "&")
    #     f.write("business_period:" + business_period_text + "&")
    #     f.write("approved_date:" + approved_date_text + "&")
    #     f.write("register_authority:" + register_authority_text + "&")
    #     f.write("used_name:" + used_name_text + "&")
    #     f.write("eng_name:" + eng_name_text + "&")
    #     f.write("business_scope:" + business_scope_text + "\n")
    return (
        ("legal_person", legal_person_texts),
        ("founded_time", founded_span),
        ("business_status", business_status_text),
        ("register_capital", register_capital_text),
        ("paid_capital", paid_capital_text),
        ("business_type", business_type_text),
        ("business_industry", business_industry_text),
        ("credit_code", credit_code_text),
        ("register_code", register_code_text),
        ("org_type", org_type_text),
        ("org_code", org_code_text),
        ("insured_num", insured_num_text),
        ("employee_num", employee_num_text),
        ("taxpayer_code", taxpayer_code_text),
        ("taxpayer_qualification", taxpayer_qualification_text),
        ("import_export_code", import_export_code_text),
        ("sea_code", sea_code_text),
        ("business_period", business_period_text),
        ("approved_date", approved_date_text),
        ("register_authority", register_authority_text),
        ("used_name", used_name_text),
        ("eng_name", eng_name_text),
        ("business_scope", business_scope_text),
    )


if __name__ == "__main__":
    process_company_detail_page("4f332f95ebdcd3c42c69a298194976b1")
    # process_company_detail_page("53e5856cfb8aac888b912efee1e24653")
    # process_company_detail_page("6f904d6f932c2f38d7219abfe0796c69")
