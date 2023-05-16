import heapq
T = 10
for test_case in range(1, T + 1):
    n=int(input())
    queue=[]
    arr=[list(map(int,input().split())) for _ in range(100)]
    # row 별 합계
    for i in range(100):
        heapq.heappush(queue,-sum(arr[i]))
    for col in range(100):
        tmp=0
        for row in range(100):
            tmp+=arr[row][col]
        heapq.heappush(queue,-tmp)
    # 대각선 합계
    tmp,tmp2=0,0
    for i in range(100):
        tmp+=arr[i][i]
        tmp2+=arr[99-i][i]
    heapq.heappush(queue,-tmp)
    heapq.heappush(queue,-tmp2)
    print(f"#{test_case} {-heapq.heappop(queue)}")