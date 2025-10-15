"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if not curr.child:
                curr = curr.next
                continue
            
            child_head = curr.child
            tail = child_head

            while tail and tail.next:
                tail = tail.next

            append = curr.next

            tail.next = append
            curr.next = child_head
            child_head.prev = curr
            if append is not None:
                append.prev = tail

            curr.child = None
            curr = curr.next
        return head
        
                
                    
            
                


        
        