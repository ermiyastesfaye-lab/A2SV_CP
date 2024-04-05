class Solution:
    def isVowel(self, letter):
        vowels = ['a', 'e', 'i', 'o', 'u']
        self.letter = letter
        return self.letter.lower() in vowels
    
    def reverseVowels(self, s):
        s = list(s)
        i, j = 0, len(s)-1
        while i < j:
            if self.isVowel(s[i]) and self.isVowel(s[j]):
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
            elif self.isVowel(s[i]):
                j-=1
            elif self.isVowel(s[j]):
                i+=1
            else:
                i+=1
                j-=1
            
        return ''.join(s)



# Example usage:
solution = Solution()
print(solution.reverseVowels("hello"))
