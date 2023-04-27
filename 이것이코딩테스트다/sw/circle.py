

T = int(input())

for _ in range(T):
    n=int(input())
    cnt=0
    for i in range(1,n):
        for j in range(1,n):
            if i*i+j*j<=n*n:
                cnt+=1
    print(n*4+1+cnt*4)