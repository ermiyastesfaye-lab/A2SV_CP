# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def validate(mid):
            count = 0
            summ = 0
            for w in weights:
                summ += w
                if summ > mid:
                    count += 1
                    summ = w
            return count + 1 <= days


        low = max(weights)
        high = sum(weights)
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2

            if validate(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

        
        


            
            

            
