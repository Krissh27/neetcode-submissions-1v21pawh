class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path=set()
        row=len(board)
        col=len(board[0])
        res=False
        def transverse(i,j,val):
            if val==len(word):
                return True
            if i<0 or j<0 or j>=col or i >=row or ((i,j) in path) or board[i][j]!=word[val]:
                
                return False
            path.add((i,j))
            res =transverse(i+1,j,val+1) or transverse(i-1,j,val+1) or transverse(i,j+1,val+1) or transverse(i,j-1,val+1)
            path.remove((i,j))
            return res

        for r in range(row):
            for c in range(col):
                if transverse(r, c, 0):
                    return True
        return res