class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cashe=[1]*(len(s)+1)
        r=len(s)
        c=len(t)
        for i in range(c-1,-1,-1):
            curr=[0]*(len(s)+1)
            for j in range(r-1,-1,-1):
                if s[j]==t[i]:
                    curr[j]=curr[j+1]+cashe[j+1]
                else:
                    curr[j]=curr[j+1]
            cashe=curr
        return cashe[0]





        