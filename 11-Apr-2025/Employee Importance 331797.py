# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        graph = defaultdict(int)
        for idx, val in enumerate(employees):
            graph[val.id] = idx
        def dfs(node):
            nonlocal ans
            ans = node.importance
            for i in node.subordinates:
                ans+=dfs(employees[graph[i]])
            return ans
        for j in employees:
            if j.id == id:
                ans += dfs(j)
                return ans
        


