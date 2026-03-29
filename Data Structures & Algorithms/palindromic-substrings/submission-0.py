class Solution:
    def countSubstrings(self, s: str) -> int:
        arr=[[False]*len(s) for i in range(len(s))]
        total=0
        for i in range(len(s)):
            for j in range(i,-1,-1):
                if s[j]==s[i]  and ((i-j)<=2 or arr[i-1][j+1]==True):
                    total+=1
                    arr[i][j]=True
        return total


        
        
        