class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

       
        cashe=[[-1]*amount for i in range(len(coins))]
        def dfs(i,a):
            if amount==a:
                return 1
            if i>=len(coins) or a>amount:
                return 0
            if cashe[i][a]!=-1:
                return cashe[i][a]
            cashe[i][a]=dfs(i,a+coins[i])+dfs(i+1,a)
            return cashe[i][a]
        return dfs(0,0)