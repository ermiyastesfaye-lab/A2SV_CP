data = input()
info = data.split()
n = int(info[0])
k = int(info[1])
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
cnt = 0
res = []

for i in range(len(list2)):
    while cnt < n and list2[i] > list1[cnt]:
        cnt += 1
    res.append(cnt)

print(" ".join(map(str, res)))
