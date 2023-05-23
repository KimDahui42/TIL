T = int(input())
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    graph=[[0] for _ in range(n+1)]
    visited=[False]*(n+1)
    answer=-1
    for i in range(m):
        x,y=map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    def dfs(start_node,cnt):
        global answer
        if answer<cnt:
            answer=cnt
        for now in graph[start_node][1:]:
            if visited[now]==False:
                visited[now]=True
                dfs(now,cnt+1)
                visited[now]=False

    for i in range(1,n+1):
        visited[i]=True
        dfs(i,1)
        visited[i]=False

    print(f"#{test_case} {answer}")
