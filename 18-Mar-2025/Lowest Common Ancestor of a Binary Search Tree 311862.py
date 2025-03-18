# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search1(node, p):
            if not node:
                return
            if node.val == p.val:
                self.ans1.append(node)
                return
            self.ans1.append(node)
            if p.val > node.val:
                return search1(node.right, p)
            elif p.val < node.val:
                return search1(node.left, p)
        def search2(node, q):
            if not node:
                return
            if node.val == q.val:
                self.ans2.append(node)
                return
            self.ans2.append(node)
            if q.val > node.val:
                return search2(node.right, q)
            elif q.val < node.val:
                return search2(node.left, q)
        self.ans1 = []
        self.ans2 = []
        res = 0
        search1(root, p)
        search2(root, q)
        for i in range(len(self.ans1)):
            if i >= len(self.ans2):
                return res
            if self.ans1[i] != self.ans2[i]:
                return res
            res = self.ans1[i]
        return res
            