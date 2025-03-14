# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            if root:
                x = 1 + dfs(root.left)
                y = 1 + dfs(root.right)
            
            return max(x, y)
        return dfs(root)