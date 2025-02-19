# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

def berni(s):
    sLst = list(s)
    left = 0
    right = len(sLst) - 1
    ans = 0
    count = 0
    sub = float('inf')
    while left < right:
        if sLst[left] != sLst[right]:
            ans += 1
            innerL = left + 1
            innerR = right
            subL = 0
            while innerL <= innerR:
                if sLst[innerL] != sLst[innerR]:
                    subL+=1
                    if sLst[innerL] == sLst[left]:
                        innerL+=1
                    elif sLst[innerR] == sLst[left]:
                        innerR-=1
                    else:
                        break      
                else:
                    innerL+=1
                    innerR-=1
            if innerL <= innerR:
                count+=1
            else:
                sub = min(sub, subL)
            innerL = left
            innerR = right - 1      
            subR = 0
            while innerL <= innerR:
                if sLst[innerL] != sLst[innerR]:
                    subR += 1
                    if sLst[innerL] == sLst[right]:
                        innerL+=1
                    elif sLst[innerR] == sLst[right]:
                        innerR-=1
                    else:
                        break
                else:
                    innerL+=1
                    innerR-=1
            if innerL <= innerR:
                count += 1
            else:
                sub = min(sub, subR)          
            if count == 2:
                return -1
            else:
                if sub != float('inf'):
                    ans += sub
            return ans
        else:
            left+=1
            right-=1
    return ans
            
    



t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(berni(s))
    