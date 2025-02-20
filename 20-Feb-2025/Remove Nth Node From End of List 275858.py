# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        while n > 0:
            right = right.next
            n-=1
        left = head
        prev = None
        while right:
            prev = left
            left = left.next
            right = right.next
        if not prev:
            head = left.next
        else:
            prev.next = left.next
        return head



