class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        def eachRow(n, ans):
            if n > rowIndex:
                return ans
            newRow = [1]
            for j in range(1, len(ans)):
                newRow.append(ans[j-1]+ans[j])
            newRow.append(1)
            ans[:] = newRow
            return eachRow(n+1, ans)
        return eachRow(1, ans)
        
        
