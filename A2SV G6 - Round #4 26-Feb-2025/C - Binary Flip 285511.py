# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

def binaryFlip(a, b):
    prefix = [0] * (n + 1)
    summ = 0
    for i in range(len(a)):
        summ += int(a[i])
        prefix[i] = summ
    flip = 0
    for i in range(len(a)-1, -1, -1):
        if flip %2 != 0:
            if a[i] == '0':
                curr = '1'
            else:
                curr = '0'
            if curr != b[i]:
                if (i + 1)/2 == prefix[i]:
                    flip+=1
                else:
                    return "NO"
        else:
             if a[i] != b[i]:
                if (i + 1)/2 == prefix[i]:
                    flip+=1
                else:
                    return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    print(binaryFlip(a, b))
   

                
            





        
            
    


