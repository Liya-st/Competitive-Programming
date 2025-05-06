# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            if node1.val > node2.val:
                node2.next = merge(node1, node2.next)
                return node2
            else:
                node1.next = merge(node1.next, node2)
                return node1

        def bin(left, right):
            if left == right:
                return lists[left]
            
            mid = (left + right) // 2
            node1 = bin(left, mid)
            node2 = bin(mid + 1, right)
            return merge(node1, node2)

        if not lists:
            return None
        else:
            return bin(0, len(lists)-1)


        