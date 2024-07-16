# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([[root, 1, 0]])
        res = 0
        prevLevel, prevValue = 0, 1
        while len(queue) > 0:
            node, value, level = queue.popleft()
            if level > prevLevel:
                prevLevel = level
                prevValue = value
            res = max(res, value - prevValue+1)
            if node.left:
                queue.append([node.left, value*2, level+1])
            if node.right:
                queue.append([node.right, value*2+1, level+1])
        return res
            
