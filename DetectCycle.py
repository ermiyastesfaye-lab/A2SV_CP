class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return None
        start = head
        while start != fast:
            start = start.next
            fast = fast.next
        return start
