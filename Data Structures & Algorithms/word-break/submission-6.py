class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ss=set()
        dp={}
        n=len(s)
        for i in wordDict:
            ss.add(i)
        


        def dfs(i,si):
            if i>=n and len(si)==0:
                return True
            if i>=n:
                return False
            if (i,si) in dp:
                return dp[(i,si)]
            si=si+s[i]
            if si in ss:
                
                
                dp[(i,si)]=dfs(i+1,si) or dfs(i+1,"") 
                return dp[(i,si)] 
            else:
                dp[(i,si)]= dfs(i+1,si)
                return dp[(i,si)]
            
        return dfs(0,"")
            

            





        