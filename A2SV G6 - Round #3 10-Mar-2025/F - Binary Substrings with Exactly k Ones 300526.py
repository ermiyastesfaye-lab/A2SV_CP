# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import defaultdict

def BinarySubstring(k, s):
    left = 0
    left2 = 0
    ans = 0
    ans2 = 0
    cnt1 = 0
    cnt2 = 0
    for right in range(len(s)):
            if s[right] == "1":
                cnt1 += 1
                cnt2+=1
            while left2 <= right and cnt2 > k-1:
                if s[left2] == "1":
                    cnt2-=1
                left2 += 1
            ans2 += right - left2 + 1 
            while left <= right and cnt1 > k:
                if s[left] == "1":
                    cnt1-=1
                left+=1
            ans += right - left + 1
    return ans - ans2
      

k = int(input())
s = input()
print(BinarySubstring(k, s))