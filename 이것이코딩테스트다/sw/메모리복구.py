T = int(input())
for test_case in range(1, T + 1):
    line=input()
    cnt=0
    for i in line:
        if cnt%2==0 and i=='1':
            cnt+=1
        elif cnt%2==1 and i=='0':
            cnt+=1
    print(f"#{test_case} {cnt}")