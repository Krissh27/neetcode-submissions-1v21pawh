class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ss=set()
        
        n=len(s)
        sl=set()
        for i in wordDict:
            ss.add(i)
            sl.add(len(i))
        dp=[-1]*(n+1)
        ll=list(sl)
        def dfs(i):
            if i==n:
                return True
            if dp[i]!=-1:
                return dp[i]
            for ii in ll:
                if (i+ii<=n) and s[i:i+ii] in ss:
                    dp[i]=dfs(i+ii)
                    if dp[i]:
                        return dp[i]
            dp[i]= False
            return dp[i]
        return dfs(0)
        


        
         
        
        
        