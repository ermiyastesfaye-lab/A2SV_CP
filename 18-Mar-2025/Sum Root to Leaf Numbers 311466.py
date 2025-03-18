# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def search(node):
            self.temp+=str(node.val)
            print("first", self.temp)
            if not node.left and not node.right:
                self.ans.append(int(self.temp))
                return
            if node.left and not node.right:
                search(node.left)
                self.temp = self.temp[:-1]
                return
            elif node.right and not node.left:
                search(node.right)
                self.temp = self.temp[:-1]
                return
            search(node.left)
            self.temp = self.temp[:-1]
            search(node.right)
            self.temp = self.temp[:-1]
        if not root:
            return
        self.ans = []
        self.temp = ""
        search(root)
        print(self.ans)
        return sum(self.ans)