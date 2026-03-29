class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j=-1
        status=True
        while j+1<len(strs[0]) and status==True:
            j=j+1
            
            for i in range(len(strs)-1):
                
                if  j>=len(strs[i+1]) or strs[i][j]!=strs[i+1][j]:
                    j=j-1
                    status=False

                    break

            
            
        return strs[0][:j+1]
                

            


        