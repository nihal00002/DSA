class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        #DLRU
        result =[]
        def solve(row,col,vp,maze,path):
            if row == len(maze) -1 and col == len(maze) -1:
                result.append(path[:])
                return 
            #for down
            if row + 1 < len(maze) and maze[row + 1][col] == 1 and vp[row + 1][col] != 1:
                
                vp[row][col] = 1
                solve(row + 1,col, vp,maze,path + "D")
                vp[row][col] = 0
            
            #for left
            if col - 1 >= 0 and maze[row][col-1] == 1 and vp[row][col-1] != 1:
                
                vp[row][col] = 1
                solve(row,col - 1, vp,maze,path + "L")
                vp[row][col] = 0
            
            #for right
            if col + 1 < len(maze) and maze[row][col + 1] == 1 and vp[row][col + 1] != 1:
                
                vp[row][col] = 1
                solve(row,col + 1,vp,maze,path + "R")
                vp[row][col] = 0
            
            #for up 
            if row - 1 >= 0 and maze[row-1][col] == 1 and vp[row-1][col] != 1:
                
                vp[row][col] = 1
                solve(row - 1, col, vp, maze, path + "U")
                vp[row][col] = 0
            return result
        
        if len(maze)== 0 or maze[0][0] == 0 or maze[len(maze)-1][len(maze)-1] == 0:
            return result
        return solve(0,0,[[0 for _ in range(len(maze))] for _ in range(len(maze))], maze,"")
                