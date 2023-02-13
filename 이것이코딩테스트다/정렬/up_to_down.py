
n=int(input())
array=sorted([int(input()) for i in range(n)],reverse=True)
for i in array:
    print(i,end=' ')