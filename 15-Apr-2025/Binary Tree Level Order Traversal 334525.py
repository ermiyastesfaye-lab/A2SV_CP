# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue= deque()
        lst = []
        idx = 0
        queue.append((root, idx))
        while queue:
            node, c_idx = queue.popleft()
            if node:
                if len(lst) > c_idx:
                    lst[c_idx].append( node.val)
                else:
                    lst.append([node.val])
                queue.append((node.left, c_idx+1))
                queue.append((node.right, c_idx+1))
        return lst
