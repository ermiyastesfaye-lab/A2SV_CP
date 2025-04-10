# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
        visited = [-1]*n
        def dfs(node):
            if visited[node] == 'w' or visited[node] == -1:
                visited[node] = 'l'
            else:
                return
            for nb in graph[node]:
                dfs(nb)
        for i in range(n):
            if visited[i] != -1:
                continue
            visited[i] = 'w'
            for j in graph[i]:
                dfs(j)
        return visited.index('w') if visited.count('w') == 1 else -1

