from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans = []
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])

        if s_count == p_count:
            ans.append(0)

        for i in range(len(p), len(s)):
            s_count[s[i]] += 1
            s_count[s[i - len(p)]] -= 1
            if s_count[s[i - len(p)]] == 0:
                del s_count[s[i - len(p)]]

            if s_count == p_count:
                ans.append(i - len(p) + 1)

        return ans
