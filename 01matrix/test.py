class TestMatrix:
    def fun(self):
        matrix = [[1000,1000,1000],[1000,1000,1000],[1000,1000,1000]]
        for i in range(3):
            for j in range(3):
                print(i,j,":",matrix[i][j])
                matrix[i][j] = 0
                print(matrix)

if __name__=='__main__':
    c = TestMatrix()
    c.fun()