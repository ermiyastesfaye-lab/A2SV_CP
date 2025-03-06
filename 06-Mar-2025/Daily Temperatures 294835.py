# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        dic = defaultdict(int)
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top = stack.pop()
                dic[top] = i
            stack.append(i)
        for i in range(len(temperatures)):
            if i in dic:
                ans[i] = dic[i] - i
            else:
                ans[i] = 0
        return ans
        