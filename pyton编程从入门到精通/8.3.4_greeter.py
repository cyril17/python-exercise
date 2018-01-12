def get_formetted_name(first_name,last_name):
    full_name = first_name + ' '+ last_name
    return full_name

while True:
    print("\nplease input your name")
    print("input 'q' to quit")
    f_name = input("First Name:")
    if f_name == 'q':
        break
    l_name = input("Last_Name:")
    if l_name == 'q':
        break

    full_name2 = get_formetted_name(f_name,l_name)
    print("\nHello " + full_name2.title())
    #print("\nHello ",full_name2.title())
    #2者都行