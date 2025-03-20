# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.curr = []
        self.sum_ = 0
        def dfs(root):
            if not root:
                return
            self.curr.append(str(root.val))
            if not root.left and not root.right:
                self.sum_ += int("".join(self.curr))
                

            dfs(root.left)
            dfs(root.right)
            self.curr.pop()

        dfs(root)
        return self.sum_ 


