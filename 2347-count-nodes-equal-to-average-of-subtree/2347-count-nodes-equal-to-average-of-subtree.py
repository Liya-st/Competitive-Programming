# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root):
            if not root:
                return (0, 0)
            if not root.left and not root.right:
                self.count +=1
                return (root.val, 1)
            left, left_depth = dfs(root.left)
            right, right_depth = dfs(root.right)
            sum_ = left + right + root.val
            depth = left_depth+right_depth+1
            if sum_ // depth == root.val:
                self.count +=1
            return sum_ , depth
        dfs(root)
        return self.count

            

        