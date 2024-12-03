from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from datetime import datetime
from lxml import etree
import os

db_config = {
    "host": "192.168.10.59",
    "user": "research",
    "password": "6usKz1Pi8aQ7q8WL",
    "database": "address-research-mater",
    "charset": "utf8mb4",
}

# db_config = {
#     "host": "127.0.0.1",
#     "user": "root",
#     "password": "10101",
#     "database": "address-research-mater",
#     "charset": "utf8mb4",
# }

DATABASE_URL = f"mysql+pymysql://{db_config.get('user')}:{db_config.get('password')}@{db_config.get('host')}" f"/{db_config.get('database')}?charset={db_config.get('charset')}"

POOL_SIZE = 10  # 连接池中的连接数
MAX_OVERFLOW = 20  # 额外可以创建的连接数
POOL_TIMEOUT = 30  # 获取连接时的最大等待时间（秒）
POOL_RECYCLE = 3600  # 自动回收连接的时间（秒），设置为-1表示不回收

engine = create_engine(
    DATABASE_URL,
    pool_size=POOL_SIZE,
    max_overflow=MAX_OVERFLOW,
    pool_timeout=POOL_TIMEOUT,
    pool_recycle=POOL_RECYCLE,
    echo=True,
)

Base = declarative_base()


class HubeiCommunity(Base):
    __tablename__ = "hubei_community"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, comment="小区名称")
    city = Column(String(255), nullable=False, comment="地级市")
    district = Column(String(255), nullable=False, comment="县、区")
    address = Column(String(255), nullable=False, comment="详细地址")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")


def add_community(model, name, city, district, address):
    session = sessionmaker(bind=engine)()
    new_community = model(
        name=name,
        city=city,
        district=district,
        address=address,
        create_time=datetime.now(),
        update_time=datetime.now(),
    )
    session.add(new_community)
    session.commit()
    session.close()
    print(f"add {name} success")


def update_community(model, name, city, district, address):
    session = sessionmaker(bind=engine)()
    session.query(model).filter(model.name == name).update(
        {
            "city": city,
            "district": district,
            "address": address,
            "update_time": datetime.now(),
        }
    )
    session.commit()
    session.close()
    print(f"update {name} success")


def get_community_list():
    session = sessionmaker(bind=engine)()
    community_list = session.query(HubeiCommunity).all()
    session.close()
    return community_list


def parse_detail_page(html_path):
    parsed_community_set = set()

    # 加载已解析的文件
    if os.path.exists("parsed_community.txt"):
        with open("parsed_community.txt", "r", encoding="utf-8") as parsed_file:
            parsed_community_set = set(parsed_file.read().splitlines())

    with open("parsed_community.txt", "a", encoding="utf-8") as parsed_file:
        # 遍历 html_path 目录下的文件
        for file in os.listdir(html_path):
            # 如果文件已经解析过，跳过
            if str(file) in parsed_community_set:
                continue

            print("==>", file)
            parsed_community_set.add(str(file))

            try:
                with open(os.path.join(html_path, file), "r", encoding="utf-8") as html_file:
                    html = html_file.read()
                    root = etree.HTML(html)

                    # 名称信息
                    name = root.xpath("//h1[@class='title']/text()")[0].strip()
                    # 位置信息
                    address = root.xpath("//p[@class='sub-title']/text()")[0].strip()
                    # 地级市
                    city = "武汉"
                    # 区、县
                    district = address.split("-")[0].strip()

                    print("名称：", name)
                    print("地级市：", city)
                    print("区、县：", district)
                    print("位置：", address)

                    add_community(HubeiCommunity, name, city, district, address)

                    parsed_file.write(str(file) + "\n")
            except Exception as e:
                print(f"Error processing file {file}: {e}")


import time


def parse_res_file(res_path):
    processed_id = set()
    if not os.path.exists("./processed_id.txt"):
        with open("./processed_id.txt", "w", encoding="utf-8") as processed_file:
            pass
    try:
        with open("./processed_id.txt", "r", encoding="utf-8") as processed_file:
            for line in processed_file:
                processed_id.add(line.strip())
        with open(res_path, "r", encoding="utf-8") as res_file, open("./processed_id.txt", "a", encoding="utf-8") as processed_file:
            for line in res_file:
                line = line.strip()

                if line == "":
                    continue

                components = line.split("/")
                id = components[0]

                if id in processed_id:
                    continue

                name = components[1]
                city = components[2]
                district = components[3]
                address = components[4]

                print("名称：", name)
                print("地级市：", city)
                print("区、县：", district)
                print("位置：", address)

                add_community(HubeiCommunity, name, city, district, address)
                processed_file.write(id + "\n")
    except Exception as e:
        print(f"Error processing file {res_path}: {e}")


if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    # parse_detail_page("./wuhan_community")
    parse_res_file("./hubei/res.txt")
    pass
