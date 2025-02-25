# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        idx = 0
        curr1 =l1
        curr2 = l2
        lst1 = []
        lst2 = []
        while curr1 and curr2:
            lst1.append(str(curr1.val))
            lst2.append(str(curr2.val))
            curr1 = curr1.next
            curr2 = curr2.next
        if curr1:
            while curr1:
                lst1.append(str(curr1.val))
                curr1 = curr1.next
        if curr2:
            while curr2:
                lst2.append(str(curr2.val))
                curr2 = curr2.next
        lst1 = list(reversed(lst1))
        lst2 = list(reversed(lst2))
        ans = int("".join(lst1)) + int("".join(lst2))
        ans = list(str(ans))
        ans = list(reversed(ans))
        dummy = ListNode()
        res = dummy
        for i in ans:
            temp = ListNode(int(i))
            res.next = temp
            res = res.next
        return dummy.next
