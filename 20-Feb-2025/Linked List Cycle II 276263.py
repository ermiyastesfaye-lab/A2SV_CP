# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = False
        slow = head
        if slow:
            slow = slow.next
        fast = head
        if fast and fast.next:
            fast = fast.next.next
        while fast and fast.next:
            if slow == fast:
                flag = True
                break
            slow = slow.next
            fast = fast.next.next
        if flag:
            slow = head
            while fast and slow:
                if fast == slow:
                    return fast
                fast = fast.next
                slow = slow.next
        else:
            return
        