# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.queue = []
        self.head = 0
    def ping(self, t: int) -> int:
        self.queue.append(t)
        while t - self.queue[self.head] > 3000:
            # self.queue.pop(0)
            self.head+=1
        return len(self.queue) - self.head
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)