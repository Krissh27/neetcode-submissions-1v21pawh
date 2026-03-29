class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res=[]
        
        def transverse(val,kk):
            if val==len(digits):
                res.append(kk)
                return 
            
            for i in (digitToChar[digits[val]]):
                transverse(val+1,kk+i)
                

                



                 
        if len(digits)>0:
            transverse(0,"")
        return res
        



                



        
            





        