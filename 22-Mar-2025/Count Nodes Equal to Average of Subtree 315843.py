# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        def rec(node):
            if not node:
                return (0, 0)
            left, nL = rec(node.left)
            right, nR = rec(node.right)
            if node.val == (left + right + node.val)//(nL+nR+1):
                self.ans += 1
            return (left + right + node.val, nL+nR+1)
        rec(root)
        return self.ans