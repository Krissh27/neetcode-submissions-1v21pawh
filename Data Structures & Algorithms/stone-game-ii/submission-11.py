class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo={}
        n=len(piles)
        def dfs(i,flag,M):
            if i >=n:
                return 0
            if (i, flag, M) in memo:
                return memo[(i, flag, M)]

            if flag:
                total=0
                res=0
                for ii in range(i,min(n,i+2*M)):
                    total+=piles[ii]
                    res=max(res,total+dfs(ii+1,not flag,max(M,ii-i+1)))
                memo[(i,flag,M)]=res
            else:
                total=0
                res=float('inf')
                for ii in range(i,min(n,i+2*M)):
                    total+=piles[ii]
                    res=min(res,dfs(ii+1,not flag,max(M,ii-i+1)))
                memo[(i,flag,M)]=res
            return res
        return dfs(0,True,1)

                
                    
                    

        