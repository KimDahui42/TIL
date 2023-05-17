T = 10
for test_case in range(1, T + 1):
    n=int(input())
    arr=[input() for _ in range(8)]
    number=0
    size=8 - (n - 1)
    ck_n=[]
    tmp=''
    for i in range(8):
        for j in range(size):
            tmp=arr[i][j:j+n]
            if tmp==tmp[::-1]:
                ck_n.append(tmp)
            tmp=''
    for i in range(8):
        for k in range(size):
            for j in range(n):
                tmp+=arr[k+j][i]
            if tmp==tmp[::-1]:
                ck_n.append(tmp)
            tmp=''
    print(f"#{test_case} {len(ck_n)}")
