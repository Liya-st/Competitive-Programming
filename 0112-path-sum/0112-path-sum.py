# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        sum_ = 0
        def helper(root, sum_):
            if not root:
                return False
            sum_ += root.val
            if not root.left and not root.right:
                return sum_ == target
            return helper(root.left, sum_) or helper(root.right, sum_)
        return helper(root, sum_)
        
    

        


        
        