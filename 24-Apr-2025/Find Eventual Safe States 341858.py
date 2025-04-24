# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0 for _ in range(len(graph))]
        ans = []
        def top(node):
            if color[node] == 1:
                color[node] == 0
                return False
            color[node] = 1
            for ngb in graph[node]:
                if color[ngb] != 2:
                    if not top(ngb):
                        return False
            print(node)            
            color[node] = 2
            ans.append(node)
            return True
        for i in range(len(graph)):
            if color[i] != 2:
                top(i)
        print(color)
        return sorted(ans)
            


