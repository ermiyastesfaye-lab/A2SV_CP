# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                new_num = num2 + num1
                stack.append(str(new_num))
            elif token == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                new_num = num2 - num1
                stack.append(str(new_num))
            elif token == "*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                new_num = num2 * num1
                stack.append(str(new_num))
            elif token == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                new_num = num2 / num1
                if new_num < 0:
                    new_num = ceil(new_num)
                else:
                    new_num = floor(new_num)
                stack.append(str(new_num))
            else:
                stack.append(token)
        return int(stack[0])
