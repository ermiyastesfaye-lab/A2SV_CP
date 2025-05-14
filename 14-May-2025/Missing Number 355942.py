# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr_xor = 0
        range_xor = 0

        for idx, num in enumerate(nums):
            arr_xor ^= num
            range_xor ^= idx + 1
        
        return range_xor ^ arr_xor


