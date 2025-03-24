# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ans = []
        self.ans1 = []
        def rec(curr, level):
            if not curr:
                return
            if len(self.ans) <= level:
                self.ans.append([])
            self.ans[level].append(curr.val)
            rec(curr.left, level + 1)
            rec(curr.right, level + 1)
        def revrec(curr, level):
            if not curr:
                return
            if len(self.ans1) <= level:
                self.ans1.append([])
            self.ans1[level].append(curr.val)
            curr.val = self.ans[level][len(self.ans1[level])-1]
            revrec(curr.left, level + 1)
            revrec(curr.right, level + 1)
        rec(root, 0)
        for i in range(len(self.ans)):
            if i%2 != 0:
                self.ans[i] = list(reversed(self.ans[i]))
        revrec(root, 0)
        return root


            
            