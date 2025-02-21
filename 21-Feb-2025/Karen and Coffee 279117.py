# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B


arr = list(map(int, input().split()))
recipes = []
ques = []
prefix =[0] * (200000 + 2)
for _ in range(arr[0]):
    lst1 = list(map(int, input().split()))
    prefix[lst1[0]-1] += 1
    prefix[lst1[1]] -= 1
    recipes.append(lst1)

for _ in range(arr[2]):
    lst2 = list(map(int, input().split()))
    ques.append(lst2)

for i in range(1, len(prefix)-1):
    prefix[i] += prefix[i - 1]
for i in range(len(prefix)-1):
    if prefix[i] >= arr[1]:
        prefix[i] = 1
    else:
        prefix[i] = 0
for i in range(1, len(prefix)-1):
    prefix[i] += prefix[i-1]

for i in ques:
    ans = prefix[i[1]-1] - prefix[i[0]-2]
    print(ans)






