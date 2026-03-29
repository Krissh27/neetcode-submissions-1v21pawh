class Solution:
    def reverseString(self, s: List[str]) -> None:
        l=0
        r=len(s)-1
        while l<r:
            s[r],s[l]=s[l],s[r]
            r=r-1
            l=l+1
        return s