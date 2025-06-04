# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 1
        def backtrack(start, path, res, m):
            if start == len(m):
                summ = sum(path)
                res.append(summ)
                return
            for end in range(start, len(m)):
                num = int(m[start:end+1])
                path.append(num)
                backtrack(end+1, path, res, m)
                path.pop()
        
        for i in range(2, n+1):
            j = i*i
            curr = str(j)
            res = []
            backtrack(0, [], res, curr)
            if i in res:
                ans += i*i
        return ans
            



