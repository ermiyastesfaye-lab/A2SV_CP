# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        dic = defaultdict(int)
        for i in answers:
            if i == 0:
                ans+=1
            elif i not in dic or i == dic[i]:
                dic[i] = 0
                ans+=i+1
            else:
                dic[i]+=1
        return ans
