class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count1=[0]*26
        count2=[0]*26
        for i in s1:
            code=ord(i)-ord("a")
            count1[code]+=1
        l,r  =0,-1
        count=0
        while r<len(s2):
            while count<(len(s1)):
                r=r+1
                code=ord(s2[r])-ord("a")
                count2[code]+=1
                
                count=count+1
            if count2==count1:
                return True
            code=ord(s2[l])-ord("a")
            count2[code]-=1
            if r+1>=len(s2):
                return False
            code=ord(s2[r+1])-ord("a")
            count2[code]+=1
            l=l+1
            r=r+1
        return False





           