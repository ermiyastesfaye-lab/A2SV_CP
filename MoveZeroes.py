lass Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
            else:
                continue
