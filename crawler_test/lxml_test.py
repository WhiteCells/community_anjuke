from lxml import etree


if __name__ == "__main__":
    xml = etree.HTML("./wuhan/2.html")

    dots = xml.xpath('//li[@class="dots"]')

    # 判断 dots 是否存在
    if dots:
        print("exist")
    else:
        print("not exist")

    print(dots)
