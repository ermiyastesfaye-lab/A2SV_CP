class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = head
        temp = head
        while temp is not None:
            if temp.next is None:
                break
            prev = prev.next
            temp = temp.next.next
        return prev
