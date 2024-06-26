import queue;

class MyStack:

    def __init__(self):
        self.q1= queue.Queue()
        self.q2 = queue.Queue()
        
        
    def push(self, x: int) -> None:
        self.q1.put(x)
        return None

    def pop(self) -> int:
        if self.q1.empty():
            return None
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        lastPop = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return lastPop
    
    def top(self) -> int:
        while not self.q1.empty():
            lastElement = self.q1.get()
            self.q2.put(lastElement)
        
        self.q1, self.q2 = self.q2, self.q1
        return lastElement
        

    def empty(self) -> bool:
        if self.q1.empty():
            return True
        return False
