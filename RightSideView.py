# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])

        while queue:
            rightSide = None
            leng = len(queue)
            for i in range(leng):
                currentNode = queue.popleft()
                if currentNode:
                    rightSide = currentNode
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)
            if rightSide:
                res.append(rightSide.val)
        return res
            
        
