


'''
#data = open("11-lyrics",encoding="utf-8").read()
#以utf-8的编码格式打开,并且读取且把他赋值给data
#print(data)
f = open("11-lyrics2",'a',encoding="utf-8")  #文件句柄，包含文件的名字大小字符集内容内存起始位置
# w 的话是新建一个空文件，会覆盖源文件！！！！！
#data = f.read()
#data2 = f.read()
#print(data)
#print('------------data2-----------',data2)
#这样的话已经读到了最后，再次读取第二次的时候，光标已经到了最底下，所以没有再次读，什么也么有读到

f.write("i was ,\n")
f.write("天安门上太阳升,\n")
#io.UnsupportedOperation: not writable
#如果用f = open("11-lyrics",encoding="utf-8")  打开文件，则会出现上面的错误，
#print(data)
data = f.read()
print('-------read-------',data)

f.close()
'''
f = open("11-lyrics",'r',encoding="utf-8")  #文件句柄，包含文件的名字大小字符集内容内存起始位置

#读出前5行
#for i in range(5):
#    print(f.readline())

#print(f.readlines())
#会把文件改为列表，每一行为一个元素
#['\ufeffSomehow, it seems the love I knew was always the most destructive kind\n', '不知为何，我经历的爱情总是最具毁灭性的的那种\n', 'Yesterday when I was young\n', '昨日当我年少轻狂\n', 'The taste of life was sweet\n', '生命的滋味是甜的\n', 'As rain upon my tongue\n', '就如舌尖上的雨露\n', 'I teased at life as if it were a foolish game\n', '我戏弄生命 视其为愚蠢的游戏\n', 'The way the evening breeze\n', '就如夜晚的微风\n', 'May tease the candle flame\n', '逗弄蜡烛的火苗\n', 'The thousand dreams I dreamed\n', '我曾千万次梦见\n', 'The splendid things I planned\n', '那些我计划的绚丽蓝图\n', 'I always built to last on weak and shifting sand\n', '但我总是将之建筑在易逝的流沙上\n', 'I lived by night and shunned the naked light of day\n', '我夜夜笙歌 逃避白昼赤裸的阳光\n', 'And only now I see how the time ran away\n', '事到如今我才看清岁月是如何匆匆流逝\n', 'Yesterday when I was young\n', '昨日当我年少轻狂\n', 'So many lovely songs were waiting to be sung\n', '有那么多甜美的曲儿等我歌唱\n', 'So many wild pleasures lay in store for me\n', '有那么多肆意的快乐等我享受\n', 'And so much pain my eyes refused to see\n', '还有那么多痛苦 我的双眼却视而不见\n', 'I ran so fast that time and youth at last ran out\n', '我飞快地奔走 最终时光与青春消逝殆尽\n', 'I never stopped to think what life was all about\n', '我从未停下脚步去思考生命的意义\n', 'And every conversation that I can now recall\n', '如今回想起的所有对话\n', 'Concerned itself with me and nothing else at all\n', '除了和我相关的 什么都记不得了\n', 'The game of love I played with arrogance and pride\n', '我用自负和傲慢玩着爱情的游戏\n', 'And every flame I lit too quickly, quickly died\n', '所有我点燃的火焰都熄灭得太快\n', 'The friends I made all somehow seemed to slip away\n', '所有我交的朋友似乎都不知不觉地离开了\n', "And only now I'm left alone to end the play, yeah\n", '只剩我一个人在台上来结束这场闹剧\n', 'Oh, yesterday when I was young\n', '噢 昨日当我年少轻狂\n', 'So many, many songs were waiting to be sung\n', '有那么那么多甜美的曲儿等我歌唱\n', 'So many wild pleasures lay in store for me\n', '有那么多肆意的快乐等我享受\n', 'And so much pain my eyes refused to see\n', '还有那么多痛苦 我的双眼却视而不见\n', "There are so many songs in me that won't be sung\n", '我有太多歌曲永远不会被唱起\n', 'I feel the bitter taste of tears upon my tongue\n', '我尝到了舌尖泪水的苦涩滋味\n', 'The time has come for me to pay for yesterday\n', '终于到了付出代价的时间 为了昨日\n', 'When I was young\n', '当我年少轻狂\n']




#low
#是把文件全部放到内存中，占内存，效率而且不高
'''
for line in f.readlines():
    print(line.strip())

#如果想要打印前9行，则
for index,line in enumerate(f.readlines):
    if index == 9:
        print('--------------')
        continue
    print(line.strip())

#readlines只适合读取小的文件
'''


#hihg bige
#在这种情况下，内存中每次只保存一行，读完一行从内存中去掉，然后读取下一行，效率高
#此种情况下文件变成了一个迭代器，
count = 0
for line in f:
    if count == 9:
        print('----------')
        count += 1
        continue
    print(line)
    count += 1
'''
计数
第8次   count =9
 9      count = 9， print(----)，count=10，然后跳出第10
'''





