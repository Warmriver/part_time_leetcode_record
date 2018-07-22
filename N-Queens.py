import copy

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []
        board = [[0 for i in range(n)] for i in range(n)]
        self.findSolution(board, ret, 0, n)
        print(len(ret))
        assert len(ret) < 1
        response = []
        for s in ret:
            # two dimensional array
            inner = []
            for s2 in s:
                for index, value in enumerate(s2):
                    if value == 1:
                        s2[index] = 'Q'
                    else:
                        s2[index] = '.'
                inner.append(''.join(i for i in s2))
            response.append(inner)
        return response

    def findSolution(self, board, ret, row, n):
        if 0 not in board[row]:
            return
        for index, c in enumerate(board[row]):
            if row == n-1:
                print("last line")
            if row == n-1 and c == 0:
                temp = copy.deepcopy(board)
                temp[row][index] = 1
                ret.append(temp)
                continue
            elif row < n -1 and c == 0:
                # good to place a queen here
                board[row][index] = 1

                # set attack path under row
                self.setAttackPath(board, row, index, n)
                return self.findSolution(board, ret, row + 1, n)
                board[row][index] = 0
        return

    def setAttackPath(self, board, row, queen_index, n):
        for next_row in range(row, len(board)):
            d = next_row - row
            if d == 0:
                for index in range(n):
                    if index != queen_index:
                        board[next_row][index] = -1
            else:
                # on left place set to attackable
                left_place = max(queen_index - d, 0)
                mid_place = queen_index
                right_place = min(queen_index + d, n - 1)
                board[next_row][left_place] = -1
                board[next_row][mid_place] = -1
                board[next_row][right_place] = -1

if __name__ == '__main__':
    s = Solution()
    ret = s.solveNQueens(4)
    print(ret)