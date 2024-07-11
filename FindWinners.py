class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        ans = {}
        for match in matches:
            for j in range(len(match)):
                if match[j] in ans.keys() and j == 1:
                    ans[match[j]] -= 1
                elif match[j] in ans.keys() and j == 0:
                    pass
                elif match[j] not in ans.keys() and j == 0:
                    ans[match[j]] = 0
                elif match[j] not in ans.keys() and j == 1:
                    ans[match[j]] = -1

        res1 = [k for k in ans.keys() if ans[k] == 0]
        res2 = [k for k in ans.keys() if ans[k] == -1]
        
        res1.sort()
        res2.sort()

        fin = [res1, res2]
        return fin
