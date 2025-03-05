# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if n == 0:
            return True
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i+1 < len(flowerbed) and flowerbed[i+1] != 1:
                    if i-1 >= 0 and flowerbed[i-1] != 1:
                        n-=1
                    elif i -1 < 0:
                        n-=1
                    elif i - 1 >=0 and flowerbed[i-1] == 1:
                        i+=1
                        continue
                elif i + 1 >= len(flowerbed):
                    if i-1 >= 0 and flowerbed[i-1] != 1:
                        n-=1
                    elif i -1 < 0:
                        n-=1   
                    elif i - 1 >=0 and flowerbed[i-1] == 1:
                        i+=1
                        continue
                i+=2
            else:
                i+=2
            if n == 0:
                return True
        return False
            


