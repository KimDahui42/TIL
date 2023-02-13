from collections import deque

def dequeDfs(graph, start):
    visited=[start]
    print()
    # 큐(queue) 구현을 위해 deque 라이브러리 사용
    queue=deque(start)
    # 큐가 빌 때까지 반복
    while queue:
        node=queue.pop()
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.extend(i)
        





def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v]=True
    print(v,end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차워 리스트)
visited=[False]*9

# 정의된 dfs 함수 호출
dfs(graph,1,visited)
dequeDfs(graph,1)