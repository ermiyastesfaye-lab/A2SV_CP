# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = defaultdict(int)
        uf = UnionFind(len(accounts))
        for idx, acc in enumerate(accounts):
            for i in range(1, len(acc)):
                if acc[i] in dic:
                    uf.union(idx, dic[acc[i]])
                dic[acc[i]] = idx
        dic2 = defaultdict(list)
        for key, val in dic.items():
            root = uf.find(val)
            dic2[root].append(key)
        result = []
        for key, val in dic2.items():
            result.append([accounts[key][0]] + sorted(val))
        return result

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0]*size
    
    def find(self, x):
        if self.root[x] == x:
            return x
        val = self.find(self.root[x])
        self.root[x] = val
        return val
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rooty] > self.rank[rootx]:
                self.root[rootx] = rooty
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1