class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ss=set()
        dp={}
        n=len(s)
        for i in wordDict:
            ss.add(i)
        


        def dfs(i,j):
            if j>=n and i>=n:
                return True
            if j>=n and i<n:
                return False
            if (i,j) in dp:
                return dp[i,j]
            if s[i:j+1] in ss and j <n:
                dp[(i,j)]= dfs(i,j+1) or dfs(j+1,j+1)
                return dp[(i,j)]
            dp[(i,j)]= dfs(i,j+1)
            return dp[(i,j)]
           
            
            
        return dfs(0,0)
            

            





        