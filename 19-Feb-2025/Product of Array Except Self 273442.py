# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums))
        prod1 = 1

        for i in range(len(nums)):
            prefix[i] = prod1
            prod1 *= nums[i]
        
        suffix = [1] * (len(nums))
        prod2 = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = prod2
            prod2 *= nums[i]
        ans = []
        
        for i in range(len(suffix)):
            ans.append(prefix[i] * suffix[i])
        
        return ans




        
