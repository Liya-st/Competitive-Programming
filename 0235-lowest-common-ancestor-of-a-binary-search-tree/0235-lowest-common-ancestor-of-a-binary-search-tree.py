# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':    
        def lca(root):
            
            if root == p or root == q:
                return root
            elif p.val < root.val and root.val < q.val or p.val > root.val and root.val > q.val:
                return root

            if root.val > p.val :
                return lca(root.left)
            elif root.val < p.val :
                return lca(root.right)
        return lca(root)