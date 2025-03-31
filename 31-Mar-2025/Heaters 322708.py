# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def validate(mid):
            i, j = 0, 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= mid:
                    i += 1
                else:
                    j += 1
            if i != len(houses):
                return False
            return True
        low, high = 0, max(houses[-1], heaters[-1])
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if validate(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans