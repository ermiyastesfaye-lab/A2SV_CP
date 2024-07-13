class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                str_part = ''
                while stack[-1] != '[':
                    str_part += stack.pop()
                stack.pop()
                
                k = ''
                while stack and stack[-1].isdigit():
                    k += stack.pop()
                repeated_str = str_part[::-1] * int(k[::-1])
                for char in repeated_str:
                    stack.append(char) 
        return ''.join(stack)
