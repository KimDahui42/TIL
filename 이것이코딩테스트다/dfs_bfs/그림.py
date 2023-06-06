from collections import deque
n,m=map(int,input().split())
arr=list()
answer,max_num,count=0,0,0
dir=[[0,1],[1,0],[0,-1],[-1,0]]
visited=[[0]*m for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int,input().split())))


def dfs(start):
    global count
    q=deque()
    q.append(start)
    while q:
        tmp=q.popleft()
        visited[tmp[0]][tmp[1]]=1
        count+=1
        for k in range(4):
            next_r,next_c=tmp[0]+dir[k][0],tmp[1]+dir[k][1]
            if next_r>=0 and next_r<n and next_c>=0 and next_c<m and arr[next_r][next_c]==1 and visited[next_r][next_c]==0:
                q.append((next_r,next_c))
                visited[next_r][next_c] = 1

for i in range(n):
    for j in range(m):
        count=0
        if visited[i][j]==0 and arr[i][j]==1:
            dfs((i,j))
            answer+=1
            max_num=max_num if count<max_num else count


print(answer)
print(max_num)

