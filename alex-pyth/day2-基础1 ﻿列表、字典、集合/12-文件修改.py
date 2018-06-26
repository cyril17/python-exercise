
import sys

'''
#将修改后的保存为新的文件
f = open("11-lyrics","r",encoding="utf-8")
f_new = open("11-lyrics.bak","w",encoding="utf-8")


for line in f:
    if "有那么多肆意的快乐等我享受" in line:
        line = line.replace("有那么多肆意的快乐等我享受","有那么多肆意的快乐等gsy享受")
    f_new.write(line)
f.close()
f_new.close()
'''


'''
#将修改后的保存为新的文件
f = open("11-lyrics","r",encoding="utf-8")
f_new = open("11-lyrics.bak","w",encoding="utf-8")

find_str = sys.argv[1]
replace_str = sys.argv[2]

for line in f:
    if find_str in replace_str:
        line = line.replace(find_str,replace_str)
    f_new.write(line)
f.close()
f_new.close()
'''




f = open("11-lyrics","r",encoding="utf-8")

with open("11-lyrics",'r',encoding="utf-8") as f:
    for line in f:
        print(line)



#python开发一般每行不超过80个字符





