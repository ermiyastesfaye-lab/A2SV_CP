# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        self.nums = nums
        summ = 0
        for i in range(len(self.nums)):
            summ += self.nums[i]
            self.prefix[i] = summ
    def sumRange(self, left: int, right: int) -> int:
        ans = self.prefix[right] - self.prefix[left-1]
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)