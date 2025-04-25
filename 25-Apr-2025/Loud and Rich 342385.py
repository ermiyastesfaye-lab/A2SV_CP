# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = [[] for _ in range(len(quiet))]
        ans = [-1] * len(quiet)
        
        for greater, lesser in richer:
            graph[lesser].append(greater)

        def dfs(node):
            if ans[node] >= 0:
                return quiet[ans[node]], ans[node]
                
            curr_min = quiet[node]
            curr_node = node
            for ngb in graph[node]:
                sub_min, sub_node = dfs(ngb)
                if sub_min < curr_min:
                    curr_min = sub_min
                    curr_node = sub_node
                    
            ans[node] = curr_node
            return curr_min, curr_node

        for node in range(len(quiet)):
            dfs(node)

        return ans