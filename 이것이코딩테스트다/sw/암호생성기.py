from collections import deque
T = 10
for test_case in range(1, T + 1):
    n=int(input())
    arr=list(map(int,input().split()))
    q=deque(arr)
    flag=True
    while flag:
        for i in range(1,6):
            left=q.popleft()-i
            left=0 if left<0 else left
            q.append(left)
            if left==0:
                flag=False
                break
    print(f"#{n} {(' ').join(list(map(str,list(q))))}")
    