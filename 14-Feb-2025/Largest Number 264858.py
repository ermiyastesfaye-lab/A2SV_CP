# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = list(map(str, nums))
        if nums.count("0") == len(nums):
            return "0"
        nums.sort(key = functools.cmp_to_key(lambda x, y: int(x+y)-int(y+x)), reverse=True)
        return "".join(nums)