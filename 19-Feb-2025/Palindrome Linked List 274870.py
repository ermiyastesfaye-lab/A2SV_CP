# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        right = head
        while right and right.next:
            left = left.next
            right = right.next.next
        prev = None
        while left:
            next_node = left.next
            left.next = prev
            prev = left
            left = next_node
        curr = head
        while prev:
            if prev.val != curr.val:
                return False
            else:
                prev = prev.next
                curr = curr.next
        return True 
        
        
        


        