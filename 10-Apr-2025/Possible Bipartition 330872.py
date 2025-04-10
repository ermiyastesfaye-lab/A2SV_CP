# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])
        visited = [None]*n
        def dfs(node, color):
            color = not color
            if visited[node - 1] and visited[node - 1] != color:
                return False
            elif visited[node - 1] and visited[node - 1] == color:
                return True
            visited[node-1] = color
            for nb in graph[node]:
                if not dfs(nb, color):
                    return False
            return True
        for i in range(1, n+1):
            if visited[i-1] == None:
                if not dfs(i, True):
                    return False
        return True

        

        