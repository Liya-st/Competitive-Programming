# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root, depth):
            if not root:
                return 
            if len(res) == depth:
                res.append(root.val)
            else:
                res[depth] = max(res[depth], root.val)
            
            dfs(root.left, depth+1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return res


        

        