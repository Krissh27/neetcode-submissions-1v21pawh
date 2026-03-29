class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        ll=len(piles)
        memo={}
        
        def dfs(i,M,s):
            if i>=ll:
                return 0
            if s == True:
                tt = 0
            else:
                tt = float('inf')
            if (i,M,s) in memo:
                return memo[(i,M,s)]
            

            for j in range(1,2*M+1):
                sumi=0
                if i+j<=ll:
                    
                    if s==True:
                        for ii in range(i,i+j):
                            sumi=sumi+piles[ii]

                        tt= max(tt,sumi+dfs(i+j,max(j,M),s==0))
                        
                    else:
                        tt= min(tt,dfs(i+j,max(j,M),s==0))
            memo[(i,M,s)]=tt
                        

            return memo[(i,M,s)]
        return dfs(0,1,True)
            