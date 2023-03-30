import heapq,sys
input=sys.stdin.readline
INF=int(1e9)

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
distance=[[INF,i] for i in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

start,goal=map(int,input().split())

def dijikstra(start):
    q=[]
    distance[start][0]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if distance[now][0]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]][0]:
                distance[i[0]][0]=cost
                distance[i[0]][1]=now
                heapq.heappush(q,(cost,i[0]))

dijikstra(start)

length,parent_node=distance[goal]
path=[goal]

while parent_node!=start:
    path.append(parent_node)
    _,parent_node=distance[parent_node]

if parent_node==start:
    path.append(parent_node)

print(length)
print(len(path))
print(" ".join(map(str,path[::-1])))
