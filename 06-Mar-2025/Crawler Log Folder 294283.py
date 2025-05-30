# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if logs[i] == "../":
                if stack:
                    stack.pop()
            elif logs[i] != "./":
                stack.append(logs[i])
        return len(stack)