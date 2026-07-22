class Solution:
    def reverse(self, x: int) -> int:
        k=abs(x)
        res=0
        while k>0:
            res=res*10+k%10
            k=k//10
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        if x<0:
            return res*-1
        return res

        