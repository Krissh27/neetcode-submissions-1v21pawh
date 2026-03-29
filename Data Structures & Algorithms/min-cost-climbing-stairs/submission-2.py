class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        nums=[float('inf')]*len(cost)

        def dfs(i):
            if i>=len(cost):
                return 0
            if nums[i]!=float('inf'):
                return nums[i]
            nums[i]= min(dfs(i+1)+cost[i],dfs(i+2)+cost[i])
            return nums[i]
        return min(dfs(0),dfs(1))
            
        
        