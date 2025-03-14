# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        if not root:
            return False

        def dfs(root):
            if not root:
                return False
            if check(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)

        def check(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return check(root.left, subRoot.left) and check(root.right, subRoot.right)

        

         
        return dfs(root)




        
        