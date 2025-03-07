# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
arr = list(map(int, input().split()))
arrS = sorted(arr)
for i in range(1, len(arr)):
    arr[i] += arr[i-1]
arr.append(0)
for i in range(1, len(arrS)):
    arrS[i] += arrS[i - 1]
arrS.append(0)
m = int(input())
question = []
for i in range(m):
    temp = list(map(int, input().split()))
    question.append(temp)
for i in question:
    if i[0] == 1:
        print(arr[i[2]-1] - arr[i[1]-2])
    else:
        print(arrS[i[2]-1] - arrS[i[1]-2])


    
