class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        for i,val in enumerate(s):
            dic[val]=i
        last=0
        count=0
        n=[]
        for i in range(len(s)):
            
            count+=1
            last=max(last,dic[s[i]])
            if last==i:
                n.append(count)
                count=0
        return n
                

            


        