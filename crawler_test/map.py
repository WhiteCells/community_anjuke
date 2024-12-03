industry_map = {
    "人工智能": "001",
    "证券": "002",
    "财务": "003",
    "投资": "004",
}


def print():
    for key, value in industry_map.items():
        print(key, value)
        # 跳过前两个


industry_map.pop()

print()
