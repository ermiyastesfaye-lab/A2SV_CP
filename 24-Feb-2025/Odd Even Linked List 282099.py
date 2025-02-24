# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = ListNode()
        even = ListNode()
        currO = head
        odd.next = currO
        currE = head.next
        even.next = currE
        idx = 1
        while currO and currE:
            if idx % 2 != 0:
                if currO:
                    currO.next = currO.next.next
                    if currO.next:
                        currO = currO.next
                        idx += 1
                    else:
                        break
            else:
                if currE:
                    currE.next = currE.next.next
                    currE = currE.next
                    idx += 1
        currO.next = even.next
        return odd.next





