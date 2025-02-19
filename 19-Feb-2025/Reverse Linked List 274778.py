# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # Dummy = ListNode(None)
        # Dummy.next = head
        prev = None
        temp = None
        curr = head
        
        while curr:
            if prev and curr:
                prev.next = temp
            temp = prev
            prev = curr
            curr = curr.next
        prev.next = temp
        if curr:
            curr.next = prev
    
        return prev



        
