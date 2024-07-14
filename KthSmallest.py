# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def traverse(root, ans):
            if root is None:
                return None
            ans.append(root.val)
            traverse(root.left, ans)
            traverse(root.right, ans)
            return ans
        res = traverse(root, ans)
        res.sort()
        return res[k-1]
