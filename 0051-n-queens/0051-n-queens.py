class Solution(object):
    def solveNQueens(self, n):
        board = ["." * n for _ in range(n)]
        result = []

        def isSafe(row, col, board, n):

            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            r, c = row, col
            while c >= 0:
                if board[r][c] == "Q":
                    return False
                c -= 1

            r, c = row, col
            while c >= 0 and r < n:
                if board[r][c] == "Q":
                    return False
                c -= 1
                r += 1
            return True

        def solve(col, board, n):
            if col == n:
                result.append(board[:])
                return
            for row in range(n):
                if isSafe(row, col, board, n):
                    board[row] = board[row][:col] + "Q" + board[row][col+1:]
                    solve(col + 1, board, n)
                    board[row] = board[row][:col] + "." + board[row][col+1:]

        solve(0, board, n)
        return result