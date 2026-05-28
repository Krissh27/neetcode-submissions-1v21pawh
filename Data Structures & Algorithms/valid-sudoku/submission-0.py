class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n=len(board)
        for i in range(n):
            row=set()
            for j in range(n):
                if board[i][j]==".":
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
        for i in range(n):
            row=set()
            for j in range(n):
                if board[j][i]==".":
                    continue
                if board[j][i] in row:
                    return False
                row.add(board[j][i])
        for i in range(n):
            row=set()
            kr=i//3
            kc=i%3
            for r in range(3):
                for j in range(3):
                    if board[kr*3+r][kc*3+j]==".":
                        continue
                    if board[kr*3+r][kc*3+j] in row:
                        return False
                    row.add(board[kr*3+r][kc*3+j])
        return True


            

        