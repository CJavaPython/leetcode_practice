from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # list : M * N grid
        # 8 neighbors
        ## live : 1
        ## dead : 0
        # four rules
        
        ## live cell
        ### live neighbor cell < 2 : dead
        ### live neighbor cell == 2, 3 : live until next generation
        ### live neighbor cell > 3 : dead

        ## dead cell
        ## live neighbor cell == 3 : live
        
        ## rule applying simultaneously
        ## return next state
        ## "in-place"

        # need to update in board -> make new state
        # 1 : live 
        # 0 : dead 
        # 2 : live to dead
        # -1 : dead to live

        # find all neighbors
        dx = [-1,-1,-1,0,0,1,1,1]
        dy = [1,0,-1,1,-1,1,0,-1]
        x_len = len(board)
        y_len = len(board[0])

        for x in range(x_len):
            for y in range(y_len):
                # neighbor count
                count = 0
                # find neighbor
                for i in range(8):
                    #check valid
                    X = x + dx[i]
                    Y = y + dy[i]
                    if (0<=X<x_len) and (0<=Y<y_len):
                        # check neighbor is live cell
                        if board[X][Y] >= 1:
                            count += 1
                # check status
                ## live cell case
                if board[x][y] == 1:
                    ## check live to dead case
                    ## live neighbor count : 2 or 3
                    ## dead : <2, >3
                    if count<2 or count>3:
                        board[x][y]=2
                ## dead cell case
                elif board[x][y] == 0:
                    ## check dead to live case
                    ## live neighbor count : 1, 2
                    if count==3:
                        board[x][y]=-1
        for x in range(x_len):
            for y in range(y_len):
                ## live to dead
                if board[x][y] == 2:
                    board[x][y] = 0
                ## dead to live
                if board[x][y] == -1:
                    board[x][y] = 1
        






s = Solution()
s.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]])


