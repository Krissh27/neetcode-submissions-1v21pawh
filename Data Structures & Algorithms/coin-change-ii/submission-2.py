class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp={}
        def dfs(i,sumi):
            if i>=n or sumi>amount:
                return 0
            if (i,sumi) in dp:
                return dp[(i,sumi)]
            
            if sumi==amount:
                return 1
            dp[(i,sumi)]= dfs(i,sumi+coins[i])+dfs(1+i,sumi)
            return dp[(i,sumi)]
        return dfs(0,0)
        