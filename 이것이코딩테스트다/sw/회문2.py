import heapq
T = 10
for test_case in range(1, T + 1):
    input()
    arr=[input() for _ in range(100)]
    q=[]
    for i in range(100):
        for j in range(100):
            tmp, row_tmp = '', ''
            for k in range(1,101-j):
                row_tmp=arr[i][j:j+k]
                tmp+=arr[j+k-1][i]
                if row_tmp==row_tmp[::-1]:
                    heapq.heappush(q,-k)
                if tmp==tmp[::-1]:
                    heapq.heappush(q,-k)
    print(f"#{test_case} {-heapq.heappop(q)}")
