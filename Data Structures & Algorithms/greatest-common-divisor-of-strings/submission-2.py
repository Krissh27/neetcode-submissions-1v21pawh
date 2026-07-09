class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1=len(str1)
        l2=len(str2)
        def divi(k):
            if l1%k!=0 or l2%k!=0:
                return False
            f1,f2=l1//k,l2//k
            return str1[:k]*f1==str1 and str1[:k]*f2==str2
        res=""
        for i in range(min(l1,l2)):
            if divi(i+1):
                res= str1[:i+1]
        return res
        