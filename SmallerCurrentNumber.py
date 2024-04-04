class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        new = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if j != i:
                    if nums[j] < nums[i]:
                        count += 1
                else:
                    continue

            new.append(count)

        return new
