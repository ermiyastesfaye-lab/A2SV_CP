# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def valid(mid):
            summ = 0
            for r in ranks:
                summ += floor(math.sqrt(mid//r))
            if summ >= cars:
                return True
            return False
        high = min(ranks) * (cars * cars)
        low = min(ranks)
        ans = float('inf')

        while low <= high:
            mid = (low + high)//2
            if valid(mid):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

            

