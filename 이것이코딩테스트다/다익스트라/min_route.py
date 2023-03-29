import heapq,sys
input=sys.stdin.readline
INF=int(1e9)

v,e=map(int,input().split())
k=int(input())

graph=[[] for _ in range(v+1)]
distance=[INF]*(v+1)

for _ in range(e):
    u,n,w=map(int,input().split())
    graph[u].append((n,w))

def dijkstra(start):
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

dijkstra(k)

for i in range(1,v+1):
    print(distance[i] if distance[i]!=INF else "INF")