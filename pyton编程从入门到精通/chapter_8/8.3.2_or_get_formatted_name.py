'''def get_formatted(first_name,middle_name,last_name):
    full_name = first_name + ' ' + middle_name + ' '+ last_name
    return full_name.title()

musician = get_formatted('cyril','guo','lee')
print(musician)
'''
def get_formatted_name(first_name,last_name,middle_name=''):

    if middle_name:
        full_name = first_name + ' '+ middle_name +' '+ last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()  #return的作用：结束一个函数的执行

musician = get_formatted_name('cyril','guo')

print(musician)

musician = get_formatted_name('cyril','guo','lee')
print(musician)