class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res=0
        dc=0

        for i in range(len(num1)-1,-1,-1):
            sc=0
            for j in range(len(num2)-1,-1,-1):
                res=res+(10**(sc+dc))*(int(num1[i])*int(num2[j]))
                sc+=1
            dc+=1
        return str(res)
                

        