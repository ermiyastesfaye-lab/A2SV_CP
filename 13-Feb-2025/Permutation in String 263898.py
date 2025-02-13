# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        left = 0
        n = len(s1)
        dic = defaultdict(int)
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            dic[s2[i]]+=1
        if dic == s1_counter:
            return True
        for right in range(n, len(s2)):
            dic[s2[left]]-=1
            if dic[s2[left]] == 0:
                del dic[s2[left]]
            dic[s2[right]]+=1
            if dic == s1_counter:
                return True
            left+=1
        return False