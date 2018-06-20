
#key value

info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}

print(info)
print(info["stu1103"])
info["stu1101"] = "武藤兰"
print(info.get("stu1105"))
print(info.get("stu1105"))