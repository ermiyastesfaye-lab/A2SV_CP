# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        income = [0 for _ in range(numCourses)]
        queue = deque()
        ans = []
        for course, pre in prerequisites:
            graph[pre].append(course)
            income[course] += 1
        for i in range(numCourses):
            if income[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            ans.append(course)
            for ngb in graph[course]:
                income[ngb] -= 1
                if income[ngb] == 0:
                    queue.append(ngb)
        if len(ans) != numCourses:
            return []
        return ans