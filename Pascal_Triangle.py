'''
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

f[x] fill storage [][]
f(5):
    for j in x:
        top_left = cache if storage[x-2][j-1] != 0 else f(x-1)[j-1]
        ...
        storage[x-1][j] = 1 if (j == 0 or j == x -1) else top_left + top_right
    return storage[x-1]


f(x, y):
    if y == 0 or y == x:
        storage[x][y] = 1
    else:

        top_left = cache if storage[x-1][j-1] != 0 else f(x-1, y-1)
        ...
        storage[x1][y] = top_left + top_right
    return storage[x][y]

'''



class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        if numRows < 1:
            return []
        storage = [[0 for col in range(row)] for row in range(1, numRows+1)]
        storage[0][0] = 1

        def gen_data(i, j):
            if j == 0 or i == j:
                storage[i][j]=1
            else:
                top_left = storage[i-1][j-1] if storage[i-1][j-1] != 0 else gen_data(i-1,j-1)
                top_right = storage[i-1][j] if storage[i-1][j] != 0 else gen_data(i-1,j)
                storage[i][j] = top_left + top_right
            return storage[i][j]
        for j_index in range(numRows):
            gen_data(numRows-1, j_index)
        print(storage)
        return storage


if __name__ == '__main__':
    s = Solution()
    s.generate(5)


