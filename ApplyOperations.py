class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i]*=2
                nums[i + 1] = 0

        count = 0
        newNums = []
        for i in range(len(nums)):
            if nums[i] == 0:
                count+=1
            else:
                newNums.append(nums[i])
        
        for j in range(count):
            newNums.append(0)
        
        return newNums
