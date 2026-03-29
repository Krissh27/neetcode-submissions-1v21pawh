class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        target=sum(piles)//2+1
        memo={}
        def dfs(i,j,sumi):
            if i>j:
                return 0
            if (i,sumi) in memo:
                return memo[(i,sumi)]
            t1=piles[i]+dfs(i+1,j,sumi+piles[i])
            t2=piles[j]+dfs(i,j-1,sumi+piles[j])
            memo[(i,sumi)]= max(t1,t2)
            return memo[(i,sumi)]
        return target<=dfs(0,len(piles)-1,0)
        