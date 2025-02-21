# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        print(count)
        hi = head
        boy = ListNode(None)
        ola = boy
        for x in range(count // k):
            for i in range(k):
                print
                if hi and ola:
                    self.insertAtBeg(ola, hi)
                    hi = hi.next
            for j in range(k):
                if ola:
                    ola = ola.next
        while hi and ola:
            ola.next = hi
            hi = hi.next
            ola = ola.next
        return boy.next

    def insertAtBeg(self, start, node):
        temp = start.next
        p = ListNode(node.val, None)
        start.next = p
        p.next = temp
