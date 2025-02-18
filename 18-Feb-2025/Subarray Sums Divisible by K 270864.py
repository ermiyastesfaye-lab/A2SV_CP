# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        curr_sum = 0
        ans = 0

        for num in nums:
            curr_sum += num
            rem = curr_sum % k
            if rem < 0:
                rem += k
            if rem in dic:
                ans += dic[rem]
                dic[rem] += 1
            else:
                dic[rem] = 1

        return ans


