T = 10
for test_case in range(1, T + 1):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for i in range(100):
        q = ''
        for j in range(100):
            if arr[j][i]==1:
                q+='1'
            elif arr[j][i]==2 and q!='':
                q+='2'
        tmp=0
        for k in range(len(q)-1):
            tmp=tmp+1 if q[k:k+2]=='12' else tmp
        cnt+=tmp
    print(f"#{test_case} {cnt}")


