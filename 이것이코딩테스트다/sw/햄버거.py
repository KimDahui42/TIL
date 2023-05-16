import heapq
T = int(input())

for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    arr=list(tuple(map(int,input().split())) for _ in range(n))
    print(arr)
    visited=[False]*len(arr)
    q=[]
    def getHamburger(currentScore,currentCal,index,visit):
        if currentCal+arr[index][1]>m:
            return heapq.heappush(q,-currentScore)
        if currentCal+arr[index][1]==m:
            return heapq.heappush(q,-currentScore+arr[index][0])
        for i in range(len(arr)):
            if not visit[i]:
                visit[i]=True
                getHamburger(currentScore+arr[index][0],currentCal+arr[index][1],i,visit)
                visit[i]=False
            
    for i in range(len(arr)):
        visited[i]=True
        getHamburger(0,0,i,visited)
        visited[i]=False

    print(f"#{test_case} {-heapq.heappop(q)}")