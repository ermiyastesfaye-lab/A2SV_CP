# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new = TreeNode(val)
        if not root:
            root = new
            return root
        curr = root
        while curr:
            if not curr.left and new.val < curr.val:
                curr.left = new
                break
            if not curr.right and new.val > curr.val:
                curr.right = new
                break
            if new.val > curr.val:
                curr = curr.right
            elif new.val < curr.val:
                curr = curr.left
        return root
       