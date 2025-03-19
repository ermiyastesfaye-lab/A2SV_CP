# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def rec(node, ans):
            if not node:
                return ans[1] - ans[0]
            if node.val > ans[1]:
                ans[1]= node.val
            if node.val < ans[0]:
                ans[0] = node.val
            ans2 = ans.copy()
            left = rec(node.left, ans)
            right = rec(node.right, ans2)
            return max(left, right)
        ans = [float('inf'), float('-inf')]
        return rec(root, ans)
            