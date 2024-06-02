class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        
        for i in path:
            if i == '..':
                if stack:
                    stack.pop()
                continue
            elif i == '.' or i == '':
                continue
            stack.append(i)
            
        return '/' +'/'.join(stack)
