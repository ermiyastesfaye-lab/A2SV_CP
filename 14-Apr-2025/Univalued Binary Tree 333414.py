# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        lst = []
        while queue:
            node = queue.popleft()
            if node and node.val != root.val:
                return False
            if node:
                lst.append(node.val)

                queue.append(node.left)
                queue.append(node.right)
        
        return True