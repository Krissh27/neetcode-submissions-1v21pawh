class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res=helper(x,n//2)
            rf=res*res
            if n%2==1:
                return rf*x
            return rf
        if n<0:
            return 1/helper(x,abs(n))
        return helper(x,abs(n))