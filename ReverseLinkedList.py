class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head
        after = temp.next
        before = None
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before
