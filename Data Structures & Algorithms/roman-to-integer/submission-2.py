class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        if len(s)==1:
            return roman[s[0]]
        l=0
        r=len(s)-2
        sumi=roman[s[-1]]
        while r>0:
            if roman[s[r]]<roman[s[r+1]]:
                sumi-=roman[s[r]]
            else:
                sumi+=roman[s[r]]
            r-=1
        
        if roman[s[0]]>=roman[s[1]]:
            sumi+=roman[s[0]]
        else:
            sumi-=roman[s[0]]
        return sumi



        