class Solution:
    def solve(self, board: List[List[str]]) -> None:
        lr,lc=len(board),len(board[0])
        dr=[(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c):
            if 0<=r<lr and 0<=c<lc and board[r][c]=="O":
                board[r][c]="t"
                for nr,nc in dr:
                    dfs(r+nr,c+nc)
            return
        for r in range(lr):
            dfs(r,0)
            dfs(r,lc-1)
        for c in range(lc):
            dfs(0,c)
            dfs(lr-1,c)
        for i in range(lr):
            for j in range(lc):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="t":
                    board[i][j]="O"

                



                





















        