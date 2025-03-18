# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def search(node):
            if not node:
                return None
            if node.val == key:
                if not node.left and not node.right:
                    return None
                elif not node.left or not node.right:
                    if node.left:
                        return node.left
                    elif node.right:
                        return node.right
                elif node.left and node.right:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    node.val = temp.val
                    temp.val = key
                    node.right = search(node.right)
                    return node
            elif node and node.val > key:
                node.left = search(node.left)
                return node
            elif node and node.val < key:
                node.right = search(node.right)
                return node
        root = search(root)
        return root
