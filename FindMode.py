# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return {}
        res = {}
        def traverse(root):
            if root.val in res:
                res[root.val]+=1
            else:
                res[root.val]=1
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(root)
        max_value = max(res.values())
        return [key for key, value in res.items() if value == max_value]
