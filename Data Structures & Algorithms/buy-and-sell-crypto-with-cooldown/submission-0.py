class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        n=len(prices)
        def dfs(i,status):
            if i>=n:
                return 0
            if status:
                memo[(i,status)]=max(-prices[i]+dfs(i+1,False),dfs(i+1,True))
            else:
                memo[(i,status)]=max(prices[i]+dfs(i+2,True),dfs(i+1,False))
            return memo[(i,status)]
        return dfs(0,True)
                

        