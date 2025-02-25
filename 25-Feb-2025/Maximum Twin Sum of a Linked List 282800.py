# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        previous = None
        curr = head
        while curr and curr.next:
            previous = curr
            curr = curr.next
            curr.prev = previous
        tail = curr
        print(tail)
        ans = 0
        while tail.next != head:
            summ = head.val + tail.val
            ans = max(summ, ans)
            head = head.next
            tail = tail.prev
        return ans
        

        