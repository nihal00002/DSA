class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        # code here
        result = []
        n = len(maze)
        def solvePath(row,col,visitedPath,path,n):
            
            if row == n - 1 and col == n - 1:
                result.append(path)
                return
            
            #for down
            if row + 1 < n and maze[row + 1][col] == 1 and visitedPath[row + 1][col] != 1:
                
                visitedPath[row][col] = 1
                
                solvePath(row +1, col,visitedPath, path +"D", n)
                
                visitedPath[row][col] = 0
            
            #for left
            if col - 1 >= 0 and maze[row][col - 1] == 1 and visitedPath[row][col - 1] != 1:
                
                visitedPath[row][col] = 1
                
                solvePath(row, col - 1, visitedPath, path + "L", n)
                
                visitedPath[row][col] = 0
            
            #for right
            if col + 1 < n and maze[row][col + 1] == 1 and visitedPath[row][col + 1] != 1:
                
                visitedPath[row][col] = 1
                
                solvePath(row, col + 1, visitedPath, path + "R", n)
                
                visitedPath[row][col] = 0
                
            #for up
            if row - 1 >= 0 and maze[row - 1][col] == 1 and visitedPath[row -1][col] != 1:
                
                visitedPath[row][col] = 1
                
                solvePath(row - 1, col, visitedPath, path + "U", n)
                
                visitedPath[row][col] = 0
                
            return result
        
        if maze[0][0] == 0:
            return result
        solvePath(0,0, [[0 for _ in range(n)] for _ in range(n)], "", n)
        
        return result
            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                