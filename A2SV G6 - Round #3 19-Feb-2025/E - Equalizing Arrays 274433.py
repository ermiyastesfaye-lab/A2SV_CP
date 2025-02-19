# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

def equalizing(arr1, arr2):
    i = 0
    j = 0
    if sum(arr1) != sum(arr2):
        return -1
    sum1 = arr1[i]
    sum2 = arr2[j]
   
    ans1 = len(arr1)
    ans2 = len(arr2)
    
    while i < len(arr1) and j < len(arr2):
        if sum1 == sum2:
            i+=1
            j+=1
            if i < len(arr1) and j < len(arr2):
                sum1 = arr1[i]
                sum2 = arr2[j]
        else:
            if sum1 < sum2:
                if i + 1 < len(arr1):
                    sum1+=arr1[i+1]
                  
                    ans1-=1
                    i+=1
                else:
                    break
            elif sum1 > sum2:
                if j + 1 < len(arr2):
                    sum2+=arr2[j+1]
                    
                    ans2-=1
                    j+=1
                else:
                    break
    if ans1 != ans2:
        return -1
    return ans1


n1 = int(input())
arr1 = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))
print(equalizing(arr1, arr2))