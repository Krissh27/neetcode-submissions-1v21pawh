class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        nums=[-1]*amount
        
        def dfs(i):
            if i > amount:
                return float('inf') 
            if i==amount:
                return 0
            kk=float('inf') 
            if nums[i]!=-1:
                return nums[i]
        
            for j in coins:
                kk=min(kk,1+dfs(i+j))
                
            nums[i]=kk
            return kk
        z=dfs(0)

        if z >= float('inf'):
            return -1
        return z


        