# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        return self.rec(curr, val)
    def rec(self, curr, val):
        if not curr:
            return None
        if curr.val == val:
            return curr
        elif curr.val > val:
            return self.rec(curr.left, val)
        else:
            return self.rec(curr.right, val)