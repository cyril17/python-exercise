def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("the file " + filename + " not exist")
        '''如果此处需要设置为失败时什么也不操作，可以
        pass  即可
        '''
    else:
        words = contents.split()
        news_world = len(words)
        print("This file" + filename + "has" + news_world + "worlds.")

filenames = ['alice.txt','pi_digits.txt']
for filename  in filenames:
    count_words(filename)

