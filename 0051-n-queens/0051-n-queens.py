class Solution(object):
    def solve(self,col,board,leftQueen,upperD,lowerD,n,result):
        if col == n:
            result.append(board[:])
            return
        for row in range(n):
            if (leftQueen[row] == 0 and lowerD[row +col] == 0 and upperD[n-1 + col - row] == 0):

                board[row] = board[row][:col] + "Q" + board[row][col + 1:]

                lowerD[row + col] = 1
                leftQueen[row] = 1
                upperD[n-1 + col - row] = 1

                self.solve(col +1, board,leftQueen,upperD,lowerD,n,result)

                board[row] = board[row][:col] + "." + board[row][col + 1:]

                lowerD[row + col] = 0
                leftQueen[row] = 0
                upperD[n - 1 + col - row] = 0
                
        return result

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        leftQueen = [0] * n
        board = ["." * n for _ in range(n)]
        upperD = [0] * (2*n-1)
        lowerD = [0] * (2*n-1)
        self.solve(0,board,leftQueen, upperD,lowerD, n,result)
        return result