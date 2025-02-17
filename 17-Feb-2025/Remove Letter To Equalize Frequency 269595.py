# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        word_c = Counter(word)
        freq = list(word_c.values())
        if max(freq) == 1:
            return True
        for i in range(len(freq)):
            freq[i]-=1
            leng = len(set(freq))
            if 0 in freq:
                leng -= 1
            if leng == 1:
                return True
            freq[i] += 1
        return False



            
            
        

        
        

        
        




