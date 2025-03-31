# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        def tree(l, r):
            if l > r:
                return None
            mid = (l+r)//2
            node = TreeNode(ans[mid])
            node.left = tree(l, mid-1)
            node.right = tree(mid+1, r)
            return node
        return tree(0, len(ans)-1)