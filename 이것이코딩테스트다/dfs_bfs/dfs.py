from collections import deque

def dfs(graph, start):
    visited=[]
    q=deque(start)
    while q:
        node=q.pop()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])
    return visited