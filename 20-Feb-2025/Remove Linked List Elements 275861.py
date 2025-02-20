# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        prev = None
        while curr:
            if curr.val == val:
                if not prev:
                    head = curr.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = prev
            else:
                prev = curr
                curr = curr.next
        return head



