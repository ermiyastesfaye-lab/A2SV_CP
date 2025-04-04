# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        def mergeSort(ans):
            left, right = 0, len(ans)-1
            mid = (left + right)//2
            if len(ans) <= 1:
                return ans
            left = mergeSort(ans[:mid+1])
            right = mergeSort(ans[mid+1:])
            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    j+=1
            while i < len(left):
                merged.append(left[i])
                i+=1
            while j < len(right):
                merged.append(right[j])
                j+=1
            return merged
        res = mergeSort(ans)
        node2 = head
        i = 0
        while node2:
            node2.val = res[i]
            node2 = node2.next
            i+=1
        return head

        
        
                


            


