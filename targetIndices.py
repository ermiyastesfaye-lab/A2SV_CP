class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        list = []
        nums.sort()
        try:
            index = nums.index(target)
            list.append(index)
        except ValueError:
            return list
        
        for i in range(index+1, len(nums)):
            if nums[i] != target:
                return list
            else:
                list.append(i)
        return list
