# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, max_, min_):
            if not node:
                return True
            
            left = valid(node.left, node.val, min_)
            right = valid(node.right, max_, node.val)

            if not left or not right:
                return False
            
            if not (min_ < node.val < max_):
                return False
            return True
        return valid(root, float("inf"), float("-inf"))
        

            

            