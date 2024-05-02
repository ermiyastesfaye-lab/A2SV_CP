class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        n= len(skill)
        left = 0
        right =  n - 1
        sum_skill = sum(skill)
        total_skill = sum_skill//(n//2)
        total_chemistry = 0
        while left < right:
            if skill[left] + skill[right] == total_skill:
                total_chemistry+=skill[left] * skill[right]
                left+=1
                right-=1
            else:
                return -1
        return total_chemistry
