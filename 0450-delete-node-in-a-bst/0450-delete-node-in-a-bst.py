# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def min_node(root):
            while root.left:
                root = root.left
            return root
        def delete(root, key):
            if not root:
                return None
            if key > root.val:
                root.right = delete(root.right, key)
            elif key < root.val:
                root.left = delete(root.left, key)
            else:
                if not root.left and not root.right:
                    return None
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                suc = min_node(root.right)
                root.val = suc.val

                root.right = delete(root.right, suc.val)
            return root
        return delete(root, key)

        