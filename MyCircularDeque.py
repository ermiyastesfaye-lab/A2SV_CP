class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class MyCircularDeque:

    def __init__(self, k: int):
        self.length = 0
        self.capacity = k
        self.first = None
        self.last = None

    def insertFront(self, value: int) -> bool:
        if self.length >= self.capacity:
            return False
        newNode = Node(value)
        if not self.first:
            self.first = newNode
            self.last = newNode
            self.length+=1
            return True
        newNode.next = self.first
        self.first.prev = newNode
        self.first = newNode
        self.length+=1
        return True
    def insertLast(self, value: int) -> bool:
        if self.length >= self.capacity:
            return False
        newNode = Node(value)
        if not self.last:
            self.first = newNode
            self.last = newNode
            self.length+=1
            return True
        temp = self.last
        self.last.next = newNode
        self.last = newNode
        newNode.prev = temp
        self.length+=1
        return True
    
    def deleteFront(self) -> bool:
        if self.length == 0:
            return False
        if self.length > 1:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length-=1
            return True
        self.first = None
        self.last = None
        self.length-=1
        return True

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False
        if self.length > 1:
            temp = self.last
            self.last = self.last.prev
            self.last.next = None
            temp.prev = None
            self.length-=1
            return True
        self.first = None
        self.last = None
        self.length-=1
        return True

    def getFront(self) -> int:
        if self.length == 0:
            return -1
        return self.first.value
    def getRear(self) -> int:
        if self.length == 0:
            return -1
        return self.last.value

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
