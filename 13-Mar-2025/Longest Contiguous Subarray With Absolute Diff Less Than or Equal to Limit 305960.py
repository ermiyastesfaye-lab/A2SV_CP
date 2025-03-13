# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        q1 = deque()
        q2 = deque()
        l = 0
        ans = 0
        for r in range(len(nums)):
            while q1 and nums[r] > q1[-1]:
                q1.pop()
            q1.append(nums[r])

            while q2 and nums[r] < q2[-1]:
                q2.pop()
            q2.append(nums[r])

            while q1[0] - q2[0] > limit:
                if q1[0] == nums[l]:
                    q1.popleft()
                if q2[0] == nums[l]:
                    q2.popleft()
                l+=1
            ans = max(ans, r - l + 1)
        return ans




