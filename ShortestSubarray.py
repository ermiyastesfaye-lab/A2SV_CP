from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque()
        n = len(nums)
        res = [0]*(n+1)
        for i in range(n):
            res[i+1] = res[i] + nums[i]
        ans = n+1
        
        for i in range(n+1):
            while queue and res[i] - res[queue[0]] >= k:
                ans = min(ans, i - queue.popleft())
            while queue and res[i] <= res[queue[-1]]:
                queue.pop()
            queue.append(i)
        return ans if ans <= n else -1
