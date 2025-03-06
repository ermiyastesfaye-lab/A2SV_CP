# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {num: -1 for num in nums2}
        stack = []
        ans  = []
        for num in nums2:
            while stack and stack [-1] < num:
                top = stack.pop()
                dic[top] = num
            stack.append(num)
        for i in nums1:
            ans.append(dic[i])
        return ans
            