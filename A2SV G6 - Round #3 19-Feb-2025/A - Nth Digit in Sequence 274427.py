# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

def nDigit(n):
    s = []
    for i in range(1, n+1):
        s.append(str(i))
    s = ''.join(s)
    return s[n-1]

n = int(input())
print(nDigit(n))