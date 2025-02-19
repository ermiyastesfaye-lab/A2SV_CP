# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
    def get(self, index: int) -> int:
        if not self.head:
            return -1
        curr = self.head
        count = 0
        while curr and count < index:
            curr = curr.next
            count += 1
        if curr:
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
       

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        if curr:
            curr.next = new_node
        curr = self.head

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if not self.head and index != 0:
            return
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        if index == 0:
            return self.addAtHead(val)
        count = 0
        while count < index - 1:
            curr = curr.next
            count += 1
        if curr:
            new_node.next = curr.next
            curr.next = new_node
        curr = self.head
    
    def deleteAtIndex(self, index: int) -> None:
        count = 0
        curr = self.head
        if self.head and index == 0:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return
        
        while curr and count < index - 1:
            curr = curr.next
            count += 1
        if curr and curr.next:
            curr.next = curr.next.next
        if curr and not curr.next:
            curr.next = None
        curr = self.head
    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)