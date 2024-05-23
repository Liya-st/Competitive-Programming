# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = ListNode(0)
        dummy.next = head

        while head:
            count +=1
            head = head.next

        prev = dummy
        for _ in range (count - n):
            prev = prev.next
        
        prev.next = prev.next.next

        return dummy.next

        
        

