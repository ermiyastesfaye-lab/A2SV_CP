# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def traverse(node):
            nonlocal ans
            if not node:
                return (0,0)
            if not node.left and not node.right:
                ans+=1
                return (node.val, 1)
            leftSum, leftCnt = traverse(node.left)
            rightSum, rightCnt = traverse(node.right)

            avg = (leftSum + rightSum+node.val)//(leftCnt+rightCnt+1)

            if avg == node.val:
                ans+=1
            return (leftSum + rightSum+ node.val, leftCnt+rightCnt+1)
        traverse(root)
        return ans
