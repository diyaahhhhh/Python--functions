def maximum(l):
    m=max(l)
    return m
L=[]
n=int(input('Enter the limit:'))
for i in range(n):
    num=int(input('Enter a number:'))
    L.append(num)
print('Maximum number:',maximum(L))