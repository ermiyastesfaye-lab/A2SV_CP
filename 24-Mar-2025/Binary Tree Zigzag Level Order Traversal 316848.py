# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        def rec(curr, level, flag):
            if not curr:
                return
            if len(self.ans) <= level:
                self.ans.append([])
            self.ans[level].append(curr.val)
            flag = not flag
            # if flag:
            rec(curr.left, level + 1, flag)
            rec(curr.right, level + 1, flag)
            # else:
            #     rec(curr.right, level + 1, flag)
            #     rec(curr.left, level + 1, flag)
        rec(root, 0, True)
        for i in range(len(self.ans)):
            if i%2 != 0:
                self.ans[i] = list(reversed(self.ans[i]))
        return self.ans


