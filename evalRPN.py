class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for i in tokens:
            if i == "+":
                if stack:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    res = num2+num1
                    stack.append(res)
            elif i == "-":
                if stack:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    res = num2-num1
                    stack.append(res)
            elif i == "*":
                if stack:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    res = num2*num1
                    stack.append(res)
            elif i == "/":
                if stack:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    res = int(num2/num1)
                    stack.append(res)
            else:
                stack.append(int(i))
        
        return stack[0]
    
solution = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(solution.evalRPN(tokens))
            
        
