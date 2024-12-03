import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

# 使用 json.dumps() 将字典转换为 JSON 字符串
data_str = json.dumps(data)

print(data_str)
