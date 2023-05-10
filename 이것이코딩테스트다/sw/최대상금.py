T = int(input())
for test_case in range(1, T + 1):
    n,m=input().split()
    m=int(m)
    n=[i for i in n]
    for i in range(len(n)-1):
        max=i
        for j in range(i+1,len(n)):
            max=max if n[max]>n[j] else j
        tmp=('').join(n)
        print(i,max,n)
        n[i],n[max]=n[max],n[i]
        if ('').join(n)!=tmp:
            m-=1
            if m==0:
                break
    # n.reverse()
    print(f"#{test_case} {('').join(n)}")