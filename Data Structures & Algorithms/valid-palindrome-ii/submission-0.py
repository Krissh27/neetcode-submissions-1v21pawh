class Solution:
    def validPalindrome(self, s: str) -> bool:
        r=len(s)-1
        l=0
        count=0
        while l<r:
            if s[l]!=s[r] and count==0:
                if s[l]==s[r-1]:
                    count=1
                    r=r-1
                elif s[l+1]==s[r]:
                    count=1
                    l=l+1
                else: 
                    return False
            elif s[l]!=s[r] and count==1:
                return False
            l,r=l+1,r-1
        return True



                

            
     
        
        