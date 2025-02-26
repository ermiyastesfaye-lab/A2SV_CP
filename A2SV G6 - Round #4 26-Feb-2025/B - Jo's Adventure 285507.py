# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B


n, m = list(map(int, input().split()))
height = list(map(int, input().split()))
prefix1 = [0]
prefix2 = [0]
for i in range(1, len(height)):
    if height[i] < height[i-1]:
        prefix1.append(height[i-1] - height[i])
    else:
        prefix1.append(0)
for i in range(len(height)-1, 0, -1):
    if height[i-1] < height[i]:
        prefix2.append(height[i] - height[i-1])
    else:
        prefix2.append(0)
for i in range(1, len(prefix1)):
    prefix1[i] += prefix1[i-1]
for i in range(1, len(prefix2)):
    prefix2[i] += prefix2[i-1]

for j in range(m):
    s, e =  list(map(int, input().split()))
    if s < e:
        print(prefix1[e-1] - prefix1[s-1])
    elif s > e:
        print(abs(prefix2[-s] - prefix2[-e]))

