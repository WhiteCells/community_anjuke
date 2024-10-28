with open("test.txt", "w", encoding="utf-8") as f:
    f.write("hello world" + "\n")
    f.write("hello world" + "\n")


with open("test.txt", "w", encoding="utf-8") as f:
    f.write("hello world" + "\n")


url = "https://wuhan.anjuke.com/community/wuchang/"
url2 = "https://wuhan.anjuke.com/community/wuchang-p2"

print(url.split("/")[-2])

# url = url.rstrip("/") + "-p2"
# print(url)


# import re

# text = "共找到 261 个小区"
# number = int(re.search(r"\d+", text).group())
# print(number)
# print(type(number))


url3 = "https://wuhan.anjuke.com/view/123123/"
# print(url3.strip("/")[-2])
print(url3.split("/")[-2])


sets = set()
sets.add(1)
sets.add(1)
sets.add(1)
sets.add(1)

for item in sets:
    print(item)
