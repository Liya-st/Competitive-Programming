# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left:
            root.left.val, root.right.val = root.right.val,root.left.val
        def dfs(root1, depth, root2):
            if not root1 or not root2:
                return
            if depth % 2 == 0:
                if root1.left and root2.left:
                    root1.left.val, root2.right.val = root2.right.val,root1.left.val
                    root1.right.val, root2.left.val = root2.left.val,root1.right.val
      
            dfs(root1.left, depth + 1, root2.right)
            dfs(root1.right, depth + 1, root2.left)
        dfs(root.left, 1, root.right)
       
        return root
            

            
            
        