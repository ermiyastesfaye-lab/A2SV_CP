# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = [[] for _ in range(len(quiet))]
        incoming = [0 for _ in range(len(quiet))]
        queue = deque()
        ans = [i for i in range(len(quiet))]
        
        for greater, lesser in richer:
            graph[greater].append(lesser)
            incoming[lesser] += 1
        
        for node in range(len(quiet)):
            if incoming[node] == 0:
                queue.append(node)
        while queue:
            node = queue.popleft()
            for ngb in graph[node]:
                if quiet[ans[node]] < quiet[ans[ngb]]:
                    ans[ngb] = ans[node]
                incoming[ngb] -= 1
                if incoming[ngb] == 0:
                    queue.append(ngb)
        return ans
            

        