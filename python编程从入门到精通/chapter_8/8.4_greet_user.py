def greet_users(names):
    for name in names:
        msg = "Hello " + name.title() + " !"
        print(msg)
usernames = ['lili','xixi','zaizai']
greet_users(usernames)