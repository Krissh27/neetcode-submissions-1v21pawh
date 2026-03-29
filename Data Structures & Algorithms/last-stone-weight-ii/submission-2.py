class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n=len(stones)
        sumi=sum(stones)
        dp={}
        def dfs(i,tt):
            if i >=n or tt>=sumi/2:
                return abs((tt-(sumi-tt)))
            
            if (i,tt) in dp:
                return dp[(i,tt)]
            dp[(i,tt)]= min(dfs(i+1,tt),dfs(i+1,tt+stones[i]))
            return dp[(i,tt)]
        return dfs(0,0)

            
            
        