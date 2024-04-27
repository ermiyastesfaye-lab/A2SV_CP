class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        count = 0
        while piles :
            count+=piles.pop(-2)
            piles.pop(0)
            piles.pop()
        return count
