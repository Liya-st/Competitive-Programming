# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def getmax(node):
            if not node:
                return 0
            nonlocal res
            left = max(0, getmax(node.left))
            right = max(0, getmax(node.right))

            res = max(left +  right + node.val, res)
            return max(left, right) + node.val
        getmax(root)
        return res