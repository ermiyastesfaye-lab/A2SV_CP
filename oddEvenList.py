class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd = head
        even_head = even = head.next
        while even and even.next:
            odd.next = odd = even.next
            even.next = even = odd.next
        odd.next = even_head
        return head
