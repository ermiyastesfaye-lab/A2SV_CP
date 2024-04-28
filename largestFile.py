class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = sorted(map(str, nums), key=lambda x: x*9, reverse=True)
        return str(int(''.join(nums)))
