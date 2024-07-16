# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        results = []
        queue.append(root)
        while len(queue) > 0:
            leng = len(queue)
            level = []
            for i in range(leng):
                currentNode = queue.popleft()
                if currentNode:
                    level.append(currentNode.val)
                    if currentNode.left is not None:
                        queue.append(currentNode.left)
                    if currentNode.right is not None:
                        queue.append(currentNode.right)
            results.append(level)
        return results
            
