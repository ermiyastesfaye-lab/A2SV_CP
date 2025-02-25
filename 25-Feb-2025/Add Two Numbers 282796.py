# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr1 =l1
        curr2 = l2
        rem = 0
        while curr1 and curr2:
            hey = curr1.val + curr2.val + rem
            rem = 0
            if hey >= 10:
                hey-=10
                rem = 1
            curr1.val = hey
            prev = curr1
            if not curr1.next and not curr2.next and rem:
                curr1.next = ListNode(1)
                return l1
            curr1 = curr1.next
            curr2 = curr2.next

        if curr1:
            while curr1:
                hey = curr1.val + rem
                rem = 0
                if hey >= 10:
                    hey-=10
                    rem = 1
                curr1.val = hey
                if not curr1.next and rem:
                    curr1.next = ListNode(1)
                    break
                curr1 = curr1.next
        if curr2:
            prev.next = curr2
            while curr2:
                hey = curr2.val + rem
                rem = 0
                if hey >= 10:
                    hey-=10
                    rem = 1
                curr2.val = hey
                if not curr2.next and rem:
                    curr2.next = ListNode(1)
                    break
                curr2 = curr2.next
        return l1