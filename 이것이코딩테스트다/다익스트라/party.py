import heapq,sys
input=sys.stdin.readline
INF=int(1e9)

n,m,x=map(int,input().split())
go_graph=[[] for _ in range(n+1)]
back_graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    go_graph[b].append((a,c))
    back_graph[a].append((b,c))

def dijikstra(start,graph):
    distance=[INF]*(n+1)
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance

go_distance=dijikstra(x,go_graph)
back_distance=dijikstra(x,back_graph)
max_heap=[]
for i in range(1,n+1):
    heapq.heappush(max_heap,-(go_distance[i]+back_distance[i]))

print(-heapq.heappop(max_heap))

