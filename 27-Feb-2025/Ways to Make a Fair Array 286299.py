# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even = []
        odd = []
        ans = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
                odd.append(0)
            else:
                even.append(0)
                odd.append(nums[i])
        for i in range(1, len(even)):
            even[i] += even[i - 1]
            odd[i] += odd[i - 1]
        for i in range(len(nums)):
            if i % 2 == 0:
                minus = even[-1] - even[i]
                minus2 = odd[-1] - odd[i]
                res1 = even[-1] - minus - nums[i] + minus2
                res2 = odd[-1] - minus2 + minus
            else:
                minus = even[-1] - even[i]
                minus2 = odd[-1] - odd[i]
                res1 = even[-1] - minus + minus2
                res2 = odd[-1] - minus2 - nums[i] + minus
                
            if res1  ==  res2:
                ans+=1

        return ans







