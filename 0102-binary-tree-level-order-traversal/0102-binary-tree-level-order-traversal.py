# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, -1)])
        lvl = 0
        dic = defaultdict(list)
        if root:
            dic[0].append(root.val)
        else:
            return []
        res =[]
        temp = 1
        while q:
            node, level = q.popleft()
            if level != lvl:
                if len(dic[lvl]) != 0:
                    res.append(dic[lvl])
                lvl +=1
                temp +=1
            if node and node.left:
                dic[temp].append(node.left.val)
                q.append((node.left, temp))
            if node and node.right:
                dic[temp].append(node.right.val)
                q.append((node.right, temp))
            # print(dic)
        if dic[lvl]:
            res.append(dic[lvl])
            
        return res

    
        