# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(set)

        for a, b in adjacentPairs:
            dic[a].add(b)
            dic[b].add(a)

        for node, conn in dic.items():
            if len(conn) == 1:
                break
        result = [node]
        while dic[node]:

            new = dic[node].pop()

            result.append(new)
            
            dic[new].remove(node)

            node = new
        return result