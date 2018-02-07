unconfirmed_users = ['first','second','third']
confirmed_users = []

"""处理用户认证操作"""
def deal_verify_user(unconfirmed_users,confirmed_users):
    while unconfirmed_users:
        """处理用户认证操作"""
        current_user = unconfirmed_users.pop()
        print("verifying User:"+current_user)
        confirmed_users.append(current_user)

def print_verify_user(confirmed_users):
    for user in confirmed_users:
        print(user.title())



deal_verify_user(unconfirmed_users,confirmed_users)

print("\nThe following users have been confirmed: ")
print_verify_user(confirmed_users)

'''
verifying User:third
verifying User:second
verifying User:first

The following users have been confirmed: 
Third
Second
First
'''
