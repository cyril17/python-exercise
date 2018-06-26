product_list = [
    ('iphone',5800),
    ('mac pro',9800),
    ('bike',800),
    ('watch',10600),
    ('coffee',31)
]

shopping_list = []

salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        #for item in product_list:
        #    print(product_list.index(item),item)
        for index,item in enumerate(product_list):
            print(index,item)

        userchoice = input("选择要买的商品：")
        if userchoice.isdigit():
            userchoice = int(userchoice)
            if userchoice < len(product_list) and userchoice >=0:
                p_item = product_list[userchoice]
                if p_item[1] <= salary: #买得起，然后将商品放入购物车列表
                  shopping_list.append(p_item)
                  salary -= p_item[1]

                  print("Added %s into shopping_cart,you current is \033[31;1m%s\033[0m" %(p_item,salary))

                else:
                    print("\033[21;1m没钱了，买不起！！，你的余额只剩下 [%s] 了\033[0m" %(salary))
            else:
                print("product code [%s] is not exist" % userchoice)

        elif userchoice == "q":
            print("---------shopping list--------")
            for p in shopping_list:
                print(p)
            print("Your current balance: %s " %(salary))
            exit()
        else:
            print("invalid option")
else:
    print("please input number")