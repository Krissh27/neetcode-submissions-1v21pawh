class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        k=columnNumber
        res=""

        while k>0:
            k-=1
            res=chr(k % 26 + ord('A'))+res
            k=k//26

            
        return res
        
        