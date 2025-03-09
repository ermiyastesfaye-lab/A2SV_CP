# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

def stot():
    s = list(input())
    t = list(input())
    p = list(input())
    if len(t) < len(s):
        return "NO"
    i = 0
    j = 0
    while j < len(t):
        if i >= len(s):
            if t[j] in p:
                idx = p.index(t[j])
                p[idx] = -1
                j+=1
            else:
                return "NO"
        else:
            if s[i] != t[j]:
                if t[j] in p:
                    idx = p.index(t[j])
                    p[idx] = None   
                    j+=1
                else:
                    return "NO"
            else:
                i+=1
                j+=1
    if i < len(s):
        return "NO"
    return "YES"          
        
t = int(input()) 
for k in range(t):
    print(stot())  
