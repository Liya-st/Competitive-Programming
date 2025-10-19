# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bal(node):
            if not node:
                return True, 0

            left, h = bal(node.left)
            right, he = bal(node.right)
            flag = left and right and abs(h - he) <=1
            return flag, 1 + max(h, he)
        return bal(root)[0]

        