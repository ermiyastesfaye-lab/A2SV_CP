# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def backtrack(nums):
            if not nums:
                return
            mid = len(nums)//2
            right = backtrack(nums[mid+1:]) 
            left = backtrack(nums[:mid])
            return TreeNode(nums[mid], left, right)
        return backtrack(nums)
            
