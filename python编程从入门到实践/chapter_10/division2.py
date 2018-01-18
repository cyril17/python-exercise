print("give me two numbers, and i'll divide them.")
print("Enter 'q' to quit.")
'''处理ZeroDivisionError异常'''

while True:
    first_number = input("please input first number:")
    if first_number == 'q':
        break
    second_number = input("please input second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
'''
运行结果
give me two numbers, and i'll divide them.
Enter 'q' to quit.
please input first number:3
please input second number:2
1.5
please input first number:5
please input second number:0
You can't divide by 0!
please input first number:
q
please input second number:
'''