class Solution:

    def encode(self, strs: List[str]) -> str:
        str1=""
        for i in strs:
            str1=str1+str(len(i))+"#"+i
        return str1



    def decode(self, s: str) -> List[str]:
        list1=[]
        i=0
        while i <len(s):
            length=0
            while s[i]!="#":
                 length=length*10+int(s[i])
                 i=i+1
            if s[i]=="#":
                 i=i+1
                 




            word=""
            for j in range(length):
                
                word=word+s[i]
                i=i+1
            
            list1.append(word)
        return list1
            
            
                

       
