# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def find_node( node):
            if not node:
                return None
            if node.val == x:
                return node
        
            return find_node(node.left) or find_node(node.right)

        def count(node):
            if node and node.val == x:
                return 0
            if node:
                return 1 + count(node.left) + count(node.right)
            
            else:
                return 0

            
        node = find_node(root)

        left = count(node.left)
        right = count(node.right)

        parent = n - left - right -1
        target = (n // 2) + 1
        if left >= target or right >= target or parent >= target:
            return True
        return False

        