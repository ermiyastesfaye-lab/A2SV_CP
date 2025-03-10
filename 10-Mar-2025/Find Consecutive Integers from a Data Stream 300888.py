# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.cnt = 0
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.cnt += 1
        if len(self.queue) < self.k:
            return False
        if len(self.queue)>self.k:
            top = self.queue.popleft()
            if top == self.value:
                self.cnt -= 1
        return self.cnt == self.k
            
            

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)