class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ss=set()
        sl=set()
        n=len(s)
        for i in wordDict:
            ss.add(i)
            sl.add(len(i))
        res=[]
       
        ll=list(sl)
        kj=[]
        def dfs(i):
            nonlocal kj
            if i==n:
                res.append(" ".join(kj))
                return None
                
            
            
            for ii in ll:
                if i+ii<=n and s[i:i+ii] in ss:
                    
                    kj.append(s[i:i+ii])
                    dfs(i+ii)
                    kj.pop()
            return None
        dfs(0)
        return res

                
                    
                            
                    

                    



        