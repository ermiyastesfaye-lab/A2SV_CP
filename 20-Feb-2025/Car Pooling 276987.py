# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[2])
        print(trips)
        prefix = [0] * (trips[-1][-1] + 2)
        for i in trips:
            prefix[i[1]]+=i[0]
            prefix[i[2]] -= i[0]
        print(prefix)
        summ = 0
        for i in range(len(prefix)-1):
            summ += prefix[i]
            prefix[i] = summ
            if prefix[i] > capacity:
                return  False
        return True