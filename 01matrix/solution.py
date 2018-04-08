"""
[
    [0, 1, 0]        [0, 1, 0]
    [0, 1, 0]   ->   [0, 1, 0]
    [1, 1, 1]        [1, 2, 1] 
]
对于每一个元素，求离他最近的0的距离
"""
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        try dp in python O(r*c)
        """
        if matrix == None or len(matrix) < 1:
            return matrix
        row = len(matrix)
        col =len(matrix[0])
        
      
        dist = [[1000] * len(matrix[0]) for i in range(len(matrix))] 
       
        """
        从右下到左上
        """
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
        
        """
        
        """
        for i in reversed(range(row)):
            for j in reversed(range(col)):
                    if i < row - 1:
                        dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                    if j < col - 1:
                        dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
        
       
        
        return dist
    def find( self,m):
        pass

if __name__ == '__main__':
    matrix = [[0,0,0],[0,1,0],[0,0,0]]
    s = Solution()
    dist = s.updateMatrix(matrix)
    print(dist)