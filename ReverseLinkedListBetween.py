# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head
        prev = None
        for _ in range(left - 1):
            prev = temp
            temp = temp.next
        before_sublist = prev
        last_node_of_sublist = temp
        current = temp
        next_node = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        if before_sublist:
            before_sublist.next = prev
        else:
            head = prev
        
        last_node_of_sublist.next = current
        
        return head
