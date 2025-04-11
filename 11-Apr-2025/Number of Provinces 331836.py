# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(set)
        for row in range(len(isConnected)):
            for col in range(len(isConnected[row])):
                if row != col and isConnected[row][col] == 1:
                    graph[row+1].add(col+1)
                    graph[col+1].add(row+1)
                if row!= col and isConnected[row][col] == 0:
                    if row+1 not in graph:
                        graph[row+1] = set()
                    if col+1 not in graph:
                        graph[col+1] = set()
        visited = set()
        cnt = 0
        def dfs(node):
            nonlocal cnt
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
        for i in range(1, len(isConnected)+1):
            if i not in visited:
                dfs(i)
                cnt+=1
        return cnt
            
            

