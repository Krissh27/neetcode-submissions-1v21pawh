class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr=[]
        for i in range(n):
            k=["."]*n
            arr.append(k)
        col=set()
        pd= set()
        nd= set()
        res=[]
        seen=set()

        def dfs(r,c):
            
            if c>=n:
                return None
            if c in col or (r-c in pd or r+c in nd):
                return None
            col.add(c)
            pd.add(r-c)
            nd.add(r+c)
            arr[r][c]="Q"
            if r>=n-1:
                res.append(["".join(row) for row in arr])
                
            for i in range(n):
              
                dfs(r+1,i)
                
            col.remove(c)
            pd.remove(r-c)
            nd.remove(r+c)
            arr[r][c]="."
            return 
        for i in range(n):
            dfs(0,i)
        return res
            


            
          
            

        