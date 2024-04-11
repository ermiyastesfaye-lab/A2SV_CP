class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return "" 
        if len(strs) == 1:
            return strs[0]
        
        k = 0
        i = 0
        prefix = ''
        min_length_string = min(strs, key=len)
        while i < len(min_length_string):
            for j in range(len(strs)):
                if strs[j][i] != strs[k][i]:
                    return prefix
            prefix += strs[k][i]
            i += 1
        return prefix
