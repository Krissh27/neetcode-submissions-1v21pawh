class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp={}
        def dfs(i,flag):
            if i >=n:
                return 0
            if (i,flag) in dp:
                return dp[(i,flag)]
            if flag:
                dp[(i,flag)]=max(-prices[i]+dfs(i+1,not flag),dfs(i+1,flag))
                return dp[(i,flag)]
            else:
                dp[(i,flag)]=max(prices[i]+dfs(i+2,not flag),dfs(i+1, flag))
                return dp[(i,flag)]
        return dfs(0,True)
            

        