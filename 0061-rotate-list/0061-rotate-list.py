
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1

        k = k % length
            
      
        last.next = head
        
       
        temp = head
        for _ in range( length - k - 1 ):
            temp = temp.next
        
        
        res = temp.next
        temp.next = None
        
        return res
