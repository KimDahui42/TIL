T = int(input())

def printing(graph):
    for i in graph:
        for j in i:
            print(j,end=' ')
        print()

for test_case in range(1, T + 1):
    n=int(input())
    graph=[[0]*n for _ in range(n)]
    cnt=0
    x,y=0,0
    for i in range(1,n*n+1):
        if cnt%4==0:
            for j in range(y,n-cnt):
                if i>n*n:
                    break
                graph[x][j]=i
                i+=1
            x,y=x+1,n-cnt-1
            for j in range(x,n-cnt):
                if i>n*n:
                    break
                graph[j][y]=i
                i+=1
            x,y=n-cnt-1,y-1
            for j in range(y,cnt-1,-1):
                if i>n*n:
                    break
                graph[x][j]=i
                i+=1
            cnt+=1
            y=cnt
    printing(graph)