class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BST(root, low=float(-inf), high=float(inf)):
            if root is None:
                return True
            if root.val <= low or root.val >= high:
                return False
            left = BST(root.left, low, root.val)
            right = BST(root.right, root.val, high)
            return left and right
        return BST(root)
