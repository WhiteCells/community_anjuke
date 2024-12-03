from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import re

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
    echo=False,
)

Base = declarative_base()


class HubeiCompany(Base):
    __tablename__ = "hubei_company"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), comment="公司名", nullable=False, unique=True)
    address = Column(String(255), comment="地址", nullable=True)
    legal_person = Column(String(64), comment="法定代表人", nullable=True)
    founded_time = Column(DateTime, comment="成立时间", nullable=True)
    business_status = Column(String(64), comment="企业经营状态", nullable=True)
    register_capital = Column(Float, comment="注册资本（万人民币）", nullable=True)
    paid_capital = Column(Float, comment="实缴资本（万人民币）", nullable=True)
    business_type = Column(String(64), comment="企业类型", nullable=True)
    business_industry = Column(String(64), comment="所属行业", nullable=True)
    credit_code = Column(String(64), comment="统一社会信用代码", nullable=True)
    register_code = Column(String(64), comment="工商注册号", nullable=True)
    org_type = Column(String(64), comment="组织机构类型", nullable=True)
    org_code = Column(String(64), comment="组织结构代码", nullable=True)
    insured_num = Column(Integer, comment="参保人数", nullable=True)
    employee_num = Column(Integer, comment="员工人数", nullable=True)
    taxpayer_code = Column(String(64), comment="纳税人识别号", nullable=True)
    taxpayer_qualification = Column(String(64), comment="纳税人资质", nullable=True)
    import_export_code = Column(String(64), comment="进出口企业代码", nullable=True)
    business_period = Column(String(64), comment="经营期限", nullable=True)
    sea_code = Column(String(64), comment="海关注册编码", nullable=True)
    approved_date = Column(DateTime, comment="核准日期", nullable=True)
    register_authority = Column(String(64), comment="登记机关", nullable=True)
    used_name = Column(String(64), comment="曾用名", nullable=True)
    eng_name = Column(String(255), comment="英文名", nullable=True)
    business_scope = Column(Text, comment="经营范围", nullable=True)


def parse_value(key, value):
    """
    根据字段类型解析值
    """
    if key in {"founded_time", "approved_date"}:
        try:
            return datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            return None
    elif key in {"register_capital", "paid_capital"}:
        try:
            return extract_number_with_unit(value)
        except ValueError:
            return None
    elif key in {"insured_num", "employee_num"}:
        try:
            return int(value)
        except ValueError:
            return None
    elif value == "--":
        return None
    return value.strip()


def add_company(model, **kwargs):
    """
    向数据库添加公司记录
    """
    session = sessionmaker(bind=engine)()
    try:
        # 检查是否已存在
        existing = session.query(model).filter_by(name=kwargs.get("name")).first()
        if existing:
            print(f"exists: {kwargs.get('name')}")
            return False

        new_company = model(**kwargs)
        session.add(new_company)
        session.commit()
        print(f"db insert: {kwargs.get('name')}")
        return True

    except IntegrityError as e:
        session.rollback()
        print(f"[IntegrityError]: {e}")

    except Exception as e:
        session.rollback()
        print(f"[Exception]: {e}")

    finally:
        session.close()


def extract_number_with_unit(s):
    """
    从字符串中提取数字
    """
    match = re.search(r"(\d+(\.\d+)?)([万亿]?)", s)
    if match:
        return float(match.group(1)) if "." in match.group(1) else int(match.group(1))
    return None


def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line == "":
                continue
            parts = line.strip().split("&")
            company_data = {}
            for part in parts:
                key, value = part.split(":", 1)
                company_data[key.strip()] = parse_value(key.strip(), value.strip())
            add_company(HubeiCompany, **company_data)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    process_file("./company/武汉.txt")
