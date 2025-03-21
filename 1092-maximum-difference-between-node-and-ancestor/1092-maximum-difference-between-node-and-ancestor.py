# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_ = float('-inf')
        min_ = float('inf')
        def dfs(root, max_, min_):
            if not root:
                return max_ - min_ 
            max_ = max(max_, root.val)
            min_ = min(min_, root.val)
            
            left = dfs(root.left, max_, min_)
            right = dfs(root.right, max_, min_)

            return max(left, right)
        return dfs(root, max_, min_)
            
        