class Solution:
    def longestPalindrome(self, s: str) -> str:
        arr=[[False]*len(s) for i in range(len(s))]
        res=0
        idx=0
        for i in range(len(s)):
            for j in range(i,-1,-1):
                if s[i]==s[j] and (i-j<=2 or arr[i-1][j+1]==True):
                   arr[i][j] = True 
                   if res<i-j+1:
                    idx=j
                    res=i-j+1
        return s[idx:idx + res]
            
        