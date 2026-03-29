class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map1={}
        l=0
        r=0
        max1=0
        max2=0
        while r<len(s):
            
            
            if s[r] in map1 and map1[s[r]]>=l:
                l=map1[s[r]]+1

            map1[s[r]]=r
            
            
            
            max2=r-l+1
            r=r+1
            max1=max(max1,max2)
        return max1

