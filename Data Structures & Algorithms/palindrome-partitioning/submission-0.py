class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        sub=[]




        def is_palindrome(k):
            r=len(k)-1
            l=0
            while l<=r:
                if k[l]!=k[r]:
                    return False
                l=l+1
                r=r-1

            return True




        def transverse(val,sk,jj):
            if val >=len(s):
                if len(s)==jj:
                    kk=sub.copy()
                    res.append(kk)
                return 


            if is_palindrome(sk+s[val]):
                sub.append(sk+s[val])
                
                transverse(val+1,"",jj=jj+len(sub[-1]))
                sub.pop()
            
            


            transverse(val+1,sk+s[val],jj)
            
        
        transverse(0,"",0)
        return res

            























            

