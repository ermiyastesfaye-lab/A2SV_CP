# Problem: The Unique Topological Sort - https://basecamp.eolymp.com/en/problems/10652

import sys
from collections import deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n+1)]
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        in_degree[b] += 1
    
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
    
    unique = True
    topo_order = []
    
    while q:
        if len(q) > 1:
            unique = False
        u = q.popleft()
        topo_order.append(u)
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    if len(topo_order) != n:
        print(-1)
    else:
        print("YES" if unique else "NO")

solve()