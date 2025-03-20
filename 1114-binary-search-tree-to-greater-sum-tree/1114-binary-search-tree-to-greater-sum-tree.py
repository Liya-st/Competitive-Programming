# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum_ = 0
        def dfs(root):
            if not root:
                return 0
            dfs(root.right)
            self.sum_ += root.val                
            root.val = self.sum_
            dfs(root.left)
        dfs(root)
        return root

    
            
            

        