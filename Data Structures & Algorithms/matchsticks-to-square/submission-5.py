class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        fsum=sum(matchsticks)
        if fsum%4!=0:
            return False
        kk=fsum//4
        res=[0]*4
        matchsticks.sort(reverse=True)
       
        def dfs(i):
            if i>=len(matchsticks):
                return True
            for j in range(len(res)):
                if res[j]+matchsticks[i]>kk:
                    continue
                res[j]+=matchsticks[i]
                mji=dfs(i+1)

                if mji:
                    return True
                

                res[j]-=matchsticks[i]
                if res[j]==0:
                    break
            return False
        
        return dfs(0)
                
                


        