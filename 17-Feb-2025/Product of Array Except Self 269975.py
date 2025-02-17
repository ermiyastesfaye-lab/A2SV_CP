# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        ans = [0] * len(nums)
        if 0 in nums:
            if nums.count(0) == 1:
                prodd = 1
                for num in nums:
                    if num != 0:
                        prodd *= num
                print(prodd)
                ans[nums.index(0)] = prodd
            return ans
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1]
        nums.append(1)
        for i in range(len(nums)-1):
            ans[i] = (nums[-2]*nums[i-1])//nums[i]
        return ans