# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target != 1:
            if maxDoubles > 0 and target % 2 == 0:
                target = target//2
                ans += 1
                maxDoubles -= 1
            elif maxDoubles > 0 and target % 2 != 0:
                target -= 1
                ans += 1
            elif maxDoubles == 0:
                ans += target - 1
                break
        return ans