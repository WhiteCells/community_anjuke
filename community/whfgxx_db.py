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


class WHFGXXCommunity(Base):
    __tablename__ = "whfgxx_community"

    id = Column(Integer, nullable=False, primary_key=True)
    province = Column(String(255), comment="省份")
    city = Column(String(255), comment="地级市")
    district = Column(String(255), comment="县、区")
    community_name = Column(String(255), comment="小区名")
    building_name = Column(String(255), comment="栋名")
    building_number = Column(String(50), comment="栋号")
    unit = Column(String(255), comment="单元")
    floor = Column(String(255), comment="楼层")
    number = Column(String(50), comment="室号")


def add_community(model, province, city, district, community_name, building_name, building_number, unit, floor, number):
    session = sessionmaker(bind=engine)()
    new_community = model(
        province=province,
        city=city,
        district=district,
        community_name=community_name,
        building_name=building_name,
        building_number=building_number,
        unit=unit,
        floor=floor,
        number=number,
    )
    session.add(new_community)
    session.commit()
    session.close()


def process_dir(dir: str):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".txt"):
                process_file(os.path.join(root, file))


def process_file(file_path):
    print(file_path)
    processed_file_keys = set()
    if not os.path.exists("./whfgxx_processed.txt"):
        with open("./whfgxx_processed.txt", "w", encoding="utf-8") as processed_file:
            pass
    with open("./whfgxx_processed.txt", "r", encoding="utf-8") as processed_file:
        for line in processed_file:
            processed_file_keys.add(line.strip())
    with open(file_path, "r", encoding="utf-8") as f, open("./whfgxx_processed.txt", "a", encoding="utf-8") as processed_file:
        content = f.read()

        province = "湖北省"
        city = "武汉市"
        # ./whfgxx\东湖高新开发区\居住项目（宝业光谷中心城108号地块）\居住项目（宝业光谷中心城108号地块）8.txt
        normalized_path = os.path.normpath(file_path)
        path_parts = normalized_path.split(os.sep)

        district = path_parts[1]
        community_name = path_parts[2]
        building_name = path_parts[3].split(".")[0]

        one_row = True
        for line in content.split("\n"):
            if one_row:
                one_row = False
                continue
            if line == "":
                continue
            components = line.split(" ")
            building_number = components[0]
            unit = components[1]
            floor = components[2]

            # number
            for i in range(3, len(components)):
                number = components[i]
                print("省份:", province)
                print("地级市:", city)
                print("区、县:", district)
                print("小区名:", community_name)
                print("栋名:", building_name)
                print("栋号:", building_number)
                print("单元:", unit)
                print("楼层:", floor)
                print("室号", number)
                print("===============")
                key = f"{province}{city}{district}{community_name}{building_name}{building_number}{unit}{floor}{number}"
                if key in processed_file_keys:
                    continue
                add_community(WHFGXXCommunity, province, city, district, community_name, building_name, building_number, unit, floor, number)
                processed_file_keys.add(key)
                processed_file.write(key + "\n")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    process_dir("./whfgxx")
