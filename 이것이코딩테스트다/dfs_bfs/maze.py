from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
    
def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nextX=x+dx[i]
            nextY=y+dy[i]
            if nextX>=n or nextX<0 or nextY>=m or nextY<0:
                continue
            if graph[nextX][nextY]==0:
                continue
            if graph[nextX][nextY]==1:
                graph[nextX][nextY]=graph[x][y]+1
                q.append((nextX,nextY))
    return graph[n-1][m-1]


print(bfs(0,0))

        


