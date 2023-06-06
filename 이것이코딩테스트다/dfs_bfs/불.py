from collections import deque

n,m=map(int,input().split())
j_idx,f_idx=(0,0),(0,0)
arr=list()
burned=[[-1]*m for _ in range(n)]
visited=[[-1]*m for _ in range(n)]

for i in range(n):
    line=input()
    tmp=list()
    for j in range(m):
        tmp.append(line[j])
        if line[j]=='J':
            j_idx=(i,j)
        elif line[j]=='F':
            f_idx=(i,j)
    arr.append(tmp)

dir=[(0,1),(1,0),(0,-1),(-1,0)]

def printing(array):
    for i in range(n):
        for j in range(m):
            print(array[i][j],end='\t')
        print()

def fire_bfs(start):
    q=deque()
    burned[start[0]][start[1]]=0
    q.append(start)
    while q:
        temp=q.popleft()
        print("=============")
        for k in range(4):
            next_r,next_c=temp[0]+dir[k][0],temp[1]+dir[k][1]
            if next_r>=0 and next_c>=0 and next_r<n and next_c<m and burned[next_r][next_c]==-1:
                burned[next_r][next_c]=burned[temp[0]][temp[1]]+1
                q.append((next_r,next_c))
        # printing(burned)
def jihun_bfs(start):
    q=deque()
    visited[start[0]][start[1]]=0
    q.append(start)
    while q:
        temp=q.popleft()
        print("=============")
        for k in range(4):
            next_r,next_c=temp[0]+dir[k][0],temp[1]+dir[k][1]
            if next_r>=0 and next_c>=0 and next_r<n and next_c<m and arr[next_r][next_c]!='#' and burned[temp[0]][temp[1]]> and visited[next_r][next_c]==-1:
                burned[next_r][next_c]=burned[temp[0]][temp[1]]+1
                q.append((next_r,next_c))


fire_bfs(f_idx)

