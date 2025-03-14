# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.ans1 = [root.val]
        self.ans2 = [root.val]
        self.recL(root.left)
        self.recR(root.right)
        if self.ans1 != self.ans2:
            return False
        return True
    def recL(self, currL):
        if not currL:
            self.ans1.append("null")
            return
        self.ans1.append(currL.val)
        self.recL(currL.left)
        self.recL(currL.right)
    def recR(self, currR):
        if not currR:
            self.ans2.append("null")
            return
        self.ans2.append(currR.val)
        self.recR(currR.right)
        self.recR(currR.left)



        