# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        dic[0] = [(0, root.val)]
        def dfs(node, row, col):
            if not node:
                return
            if node.left:
                dic[row - 1].append((col + 1, node.left.val))
                dfs(node.left, row -1, col + 1)
            if node.right:
                dic[row + 1].append((col +1, node.right.val))
                dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)
        res= []
        for k, v in sorted(dic.items()):
            if len(v) == 1:
                res.append([v[0][1]])
            else:
                temp = []
                for n in sorted(v):
                    temp.append(n[1])
                res.append(temp)
        return res

                