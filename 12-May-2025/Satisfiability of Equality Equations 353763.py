# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for i in range(len(equations)):
            x = ord(equations[i][0])-97
            y = ord(equations[i][-1])-97
            if equations[i][1] == '=':
                uf.union(x, y)
        for i in range(len(equations)):
            x = ord(equations[i][0])-97
            y = ord(equations[i][-1])-97
            if equations[i][1] != '=':
                if uf.find(x) == uf.find(y):
                    return False    
        return True
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