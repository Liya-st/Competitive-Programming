# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        rev = False

        q = deque([root])
        if not root:
            return []

        while q:
            temp = []
            arr = q
            q = deque()
            for _ in range(len(arr)):
                if rev:
                    node = arr.pop()        
                else:
                    node = arr.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            rev = not rev 
            res.append(temp)
        return res
            

        