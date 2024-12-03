import re

text1 = "20万"
text2 = "20元"
text3 = "20"

pattern = r"\d+(\.\d+)?(万|元)"

matches1 = re.findall(pattern, text1)
matches2 = re.findall(pattern, text2)
matches3 = re.findall(pattern, text3)
# print(matches1)
# print(matches2)
# print(matches3)
if matches2:
    print("2")
if matches3:
    print("-")
