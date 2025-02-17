# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lst1 = [0]*(len(s) + 1)
        for i in range(len(s)):
            lst1[i] = ord(s[i])
        lst = [0] * (len(s) + 1)
        for j in shifts:
            if j[2] == 0:
                lst[j[0]] -= 1
                lst[j[1] + 1] += 1
            else:
                lst[j[0]] += 1
                lst[j[1] + 1] -= 1
        lst[-1] = 0
        for k in range(1, len(lst)-1):
            lst[k]+=lst[k-1]
        for w in range(len(lst1)):
            lst1[w]+=lst[w]
            print("before", lst1[w])
            while lst1[w] > 122:
                lst1[w] = 96 + (lst1[w] - 122)
            while lst1[w] < 97:
                lst1[w] = 123 - (97 - lst1[w] )
            print("after", lst1[w])
            lst1[w] = chr(lst1[w])
        return "".join(lst1[:len(lst1)-1])


        
