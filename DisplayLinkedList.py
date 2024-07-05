class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")

    def get(self, index: int) -> int:
        if self.length == 0 or index < 0 or index >= self.length:
            return -1
        temp = self.head
        for _ in range(index):
            if temp is None:
                return -1
            temp = temp.next
        return temp.val if temp else -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            newNode = Node(val)
            temp = self.head
            for _ in range(index - 1):
                if temp is None:
                    return
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                if prev is None:
                    return
                prev = prev.next
            if index == self.length - 1:
                self.tail = prev
            prev.next = prev.next.next if prev.next else None
        self.length -= 1
