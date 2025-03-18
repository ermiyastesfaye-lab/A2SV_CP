# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.rec(root, 0)
        return self.ans
    def rec(self, curr, level):
        if not curr:
            return
        if len(self.ans) <= level:
            self.ans.append(float('-inf'))
        self.ans[level] = max(curr.val, self.ans[level])
        self.rec(curr.left, level + 1)
        self.rec(curr.right, level + 1)
        