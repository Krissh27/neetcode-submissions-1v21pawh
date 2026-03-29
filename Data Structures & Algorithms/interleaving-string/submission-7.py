class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo={}
        sl1=(len(s1))
        sl2=(len(s2))
        sl3=len(s3)
        if (sl1+sl2)!=sl3:
            return False  
        def dfs(i,j,k):
            if k==sl3:
                return True
            if (i,j) in memo:
                return memo[(i,j)]

            if i<sl1 and s1[i]==s3[k]:
                if dfs(i+1,j,k+1):
                    memo[(i,j)]=True
                    return memo[(i,j)]

            if j<sl2 and s2[j]==s3[k]:
                if dfs(i,j+1,k+1):
                    memo[(i,j)]=True
                    return memo[(i,j)]
                
            memo[(i,j)]= False
            return memo[(i,j)]
        return dfs(0,0,0)
            

