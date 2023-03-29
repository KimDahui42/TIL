import heapq

INF=int(1e9)

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost))

start,goal=map(int,input().split())

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

dijkstra(start)

print(distance[goal])