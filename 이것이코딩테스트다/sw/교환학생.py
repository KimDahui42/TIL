T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    arr=list(map(int,input().split()))
    cnt=arr.count(1)
    answer,current=0,0
    flag=True if n%cnt==0 else False
    print(cnt)
    answer=current=n//cnt-1 if flag else n//cnt
    answer*=7
    for i in arr:
        print(i,answer,current)
        if i==1:
            current+=1
            if current==n:
                break
        answer+=1
    print(f"#{test_case} {answer}")
    
