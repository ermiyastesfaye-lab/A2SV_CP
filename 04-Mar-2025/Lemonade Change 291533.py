# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tot = defaultdict(int)
        total = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                tot[5]+=1
                continue
            if bills[i] == 10:
                if 5 in tot:
                    tot[5] -= 1
                    if tot[5] == 0:
                        del[tot[5]]
                else:
                    return False
            if bills[i] == 20:
                if 5 in tot and 10 in tot:
                    tot[5] -= 1
                    if tot[5] == 0:
                        del tot[5]
                    tot[10]-=1
                    if tot[10] == 0:
                        del tot[10]
                elif tot[5] >= 3:
                    tot[5]-=3
                    if tot[5] == 0:
                        del tot[5]
                else:
                    return False
            tot[bills[i]]+=1
        return True
