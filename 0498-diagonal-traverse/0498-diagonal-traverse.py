class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        dic = defaultdict(list)
        res = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                dic[row+col].append(mat[row][col])
        
        for key, value in dic.items():
            if key % 2 == 0:
                res.extend(value[::-1])
            else:
                res.extend(value)
        return res
        
            
    
        