class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        max_freq=0
        res=0

        map1={}
        while r<len(s):
            map1[s[r]]= 1 + map1.get(s[r], 0)
            max_freq=max(max_freq,map1[s[r]])
            while r-l+1-max_freq>k :
                map1[s[l]]-=1
                max_freq=max(max_freq,map1[s[l]])
                l=l+1
            res=max(res,r-l+1)
            r=r+1
            
        return res
            
            





        