# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root: return 0,0
            left,ln = dfs(root.left)
            right,rn = dfs(root.right)
            if(root.val+left+right)//(ln+rn+1) == root.val:
                self.ans += 1
            return root.val+left+right,ln+rn+1
        dfs(root)
        return self.ans
            
