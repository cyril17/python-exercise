data = {

    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{"oldboy","test.yaml"},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{"链家地产","我爱我家"},
        },
        '朝阳':{
            "望京":["奔驰","陌陌"],
            "国贸": ["CICC","HP"],
            "东直门": ["Advent","飞信"],
        },
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

exit_flag = False    #标志位

while not exit_flag:
    for i in data:
        print(i)

    choice = input("选择进入1：")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("选择进入2：")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t",i3)
                    choice3 = input("选择进入3")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t", i4)
                        choice4 = input("最后一层，按b返回：")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True