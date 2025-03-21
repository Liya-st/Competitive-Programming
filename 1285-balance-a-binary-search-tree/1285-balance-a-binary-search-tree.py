# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            tree.append(root.val)
            inorder(root.right)
        inorder(root)

        def balance(left, right):
            if left > right:
                return
            mid = (left + right) //2
            l = balance(left, mid-1)
            r = balance(mid+1, right)

            return TreeNode(tree[mid], l, r)
        return balance(0, len(tree)-1)
        

        