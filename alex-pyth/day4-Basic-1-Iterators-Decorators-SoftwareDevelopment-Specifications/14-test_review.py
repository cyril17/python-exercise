
a = [1,2,3,4,5,6,7,8,9,10]
b=[]

for i in a:
    b.append(i+1)

a = b
print(a)

print('------------------------------------')

for index,i in enumerate(a):
    a[index] +=1

print(a)
print('------------------------------------')

a = map(lambda x:x+1,a)
b=[]
for i in a:
    b.append(i)
print(b)
print('------------------------------------')

#a = [1,2,3,4,5,6,7,8,9,10]
#print(a)
a = （i+1 for i in range(1,11))
print(a)

