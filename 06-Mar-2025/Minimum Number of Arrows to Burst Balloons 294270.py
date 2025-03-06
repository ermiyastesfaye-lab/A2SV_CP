# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        i = 0
        ans = 0
        while i < len(points):
            right = points[i][1]
            while i + 1 < len(points) and right >= points[i+1][0]:
                i+=1
            i+=1
            ans+=1
        return ans

