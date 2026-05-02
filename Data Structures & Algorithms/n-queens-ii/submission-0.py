class Solution:
    def totalNQueens(self, n: int) -> int:
        arr=[]
        for i in range(n):
            k=["."]*n
            arr.append(k)
        col=set()
        pd=set()
        nd=set()
        res=[]
        count=0
        def dfs(r):
            nonlocal count
            if r==n:
                count+=1
                return
            for i in range(n):
                if i in col or (r-i) in pd or (r+i) in nd:
                    continue
                col.add(i)
                pd.add(r-i)
                nd.add(r+i)

                dfs(r+1)
                col.remove(i)
                pd.remove(r-i)
                nd.remove(r+i)
            return 
        dfs(0)
        return count


            

        