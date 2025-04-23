class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[0 for _ in range(len(image[0]))]for _ in range(len(image))]
        visited = [[False for _ in range(len(image[0]))]for _ in range(len(image))]

        init = image[sr][sc]
        image[sr][sc] = color
        
        def inbound(i, j):
            return 0 <= i < len(image) and 0 <= j < len(image[0]) 

        q = deque([(sr, sc)])
        while q:
            i, j = q.popleft()
            for row, col in offset:
                row += i
                col += j
                if inbound(row, col) and image[row][col] == init and not visited[row][col]:
                    image[row][col] = color
                    visited[row][col] = True
                    q.append((row, col))
        return image
            

        