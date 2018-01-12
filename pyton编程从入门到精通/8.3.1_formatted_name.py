def get_formatted(firs_name,last_name):
    """返回干净整洁的姓名"""
    full_name = firs_name + ' ' + last_name
    return full_name.title()

musician = get_formatted('cyril','guo')
print(musician)