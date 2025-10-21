# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        front, cur =dummy, head
        if r==l:
            return head

        for _ in range(l-1):
            front, cur = cur, cur.next
        prev = None
        next_ = cur
        for _ in range(r-l+1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        front.next = prev
        next_.next = cur
        return dummy.next

        
        