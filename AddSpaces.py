class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result = []
        idx = 0   

        for i, char in enumerate(s):
            if idx < len(spaces) and i == spaces[idx]:
                result.append(' ')
                idx+=1
            result.append(char)
        
        return ''.join(result)
