# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        dic1  = defaultdict(int)
        dic2 = defaultdict(int)
        ans = []
        for query in queries:
            if dic1[query[0]] and dic1[query[0]]!=query[1]:
                dic2[dic1[query[0]]]-=1
                if dic2[dic1[query[0]]] == 0:
                    del dic2[dic1[query[0]]]
            dic2[query[1]]+=1
            if dic1[query[0]] and dic1[query[0]]==query[1]:
                dic2[query[1]]-=1
            dic1[query[0]] = query[1]
            ans.append(len(dic2.keys()))
        return ans

            
