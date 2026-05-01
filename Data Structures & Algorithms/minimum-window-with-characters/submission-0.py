class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        if m>n:
            return ""
        target={}
        for i in t:
            if i not in target:
                target[i]=0
            target[i]+=1
        check={}
        count=0
        targetc=len(target)
        l=0
        reslen=float('inf')
        fl,fr=0,0
        for i in range(n):
            check[s[i]]=1+check.get(s[i], 0)
            if s[i] in target and target[s[i]]==check[s[i]]:
                count+=1
            while count==targetc:
                res=i-l+1
                if res<reslen:
                    reslen=res
                    fl=l
                    fr=i
                check[s[l]]-=1
                if s[l] in target and check[s[l]]<target[s[l]]:
                    count-=1
                l+=1
        if reslen!=float('inf'):
            return s[fl:fr+1]
        return ""
        

            

                
            

        
            



            







        