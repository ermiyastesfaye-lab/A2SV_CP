# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    def push(self, x: int) -> None:
        self.queue1.append(x)
    def pop(self) -> int:
        if self.empty():
            return False
        if self.queue1:
            while self.queue1:
                if len(self.queue1) == 1:
                    return self.queue1.popleft()
                self.queue2.append(self.queue1.popleft())
        elif self.queue2:
             while self.queue2:
                if len(self.queue2) == 1:
                    return self.queue2.popleft()
                self.queue1.append(self.queue2.popleft())
    def top(self) -> int:
        if self.empty():
            return False
        if self.queue1:
            while self.queue1:
                if len(self.queue1) == 1:
                    top = self.queue1.popleft()
                    self.queue2.append(top)
                    return top
                self.queue2.append(self.queue1.popleft())
        elif self.queue2:
             while self.queue2:
                if len(self.queue2) == 1:
                    top = self.queue2.popleft()
                    self.queue1.append(top)
                    return top
                self.queue1.append(self.queue2.popleft())
    def empty(self) -> bool:
        if self.queue1 or self.queue2:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()