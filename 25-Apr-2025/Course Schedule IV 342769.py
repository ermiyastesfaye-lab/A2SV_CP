# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        graph2 = [set() for _ in range(numCourses)]
        queue = deque()
        ans = []
        for pre, course in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()

            for ngb in graph[course]:
                graph2[ngb].add(course)
                graph2[ngb].update(graph2[course])
                incoming[ngb]-=1
                if incoming[ngb] == 0:
                    queue.append(ngb)
        ans = []
        for u, v in queries:
            if u in graph2[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans




            


