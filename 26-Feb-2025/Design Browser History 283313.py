# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class Node:
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head
    def visit(self, url: str) -> None:
        newNode = Node(url)
        newNode.prev = self.curr
        self.curr.next = newNode
        self.curr = self.curr.next
    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev == None:
                return self.curr.val
            self.curr = self.curr.prev
        return self.curr.val
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next == None:
                return self.curr.val
            self.curr = self.curr.next
        return self.curr.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)