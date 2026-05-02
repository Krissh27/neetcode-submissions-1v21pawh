class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ss=set()
        sl=set()
        n=len(s)
        for i in wordDict:
            ss.add(i)
            sl.add(len(i))
        ll=list(sl)
            
        
        dp={}
       
        ll=list(sl)
        kj=[]
        def dfs(i):
            if i==n:
                return [""]
            if i in dp:
                return dp[i]
            res=[]
            for ii in ll:
                if i+ii<=n and s[i:i+ii] in ss:
                    kk=dfs(i+ii)
                    for ik in kk:
                        if ik =="":
                            res.append(s[i:i+ii])
                        else:
                            res.append(s[i:i+ii]+" "+ik)
            dp[i]=res
            return res
        return dfs(0)
                
            

        