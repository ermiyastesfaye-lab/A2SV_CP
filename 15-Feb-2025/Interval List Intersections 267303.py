# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        pnt_1 = 0
        pnt_2 = 0
        while pnt_1 < len(firstList) and pnt_2 < len(secondList):
            i = max(firstList[pnt_1][0], secondList[pnt_2][0])
            j = min(firstList[pnt_1][1], secondList[pnt_2][1])
            if i <= j:
                intersections.append([i, j])
            if firstList[pnt_1][1] < secondList[pnt_2][1]:
                pnt_1+=1
            else:
                pnt_2+=1
        return intersections
