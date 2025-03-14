# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        self.ans = []
        self.rec(curr)
        return self.ans
    def rec(self, curr):
        if not curr:
            return
        self.ans.append(curr.val)
        self.rec(curr.left)
        self.rec(curr.right)
        