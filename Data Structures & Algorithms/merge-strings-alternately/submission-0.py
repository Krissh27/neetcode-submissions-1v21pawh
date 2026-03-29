class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        i=0
        while i< min(len(word1),len(word2)):
            result=result+word1[i]+ word2[i]
            i=i+1
        while i< max(len(word1),len(word2)):
            if i >=len(word1):
                result=result + word2[i]
            elif i>=len(word2):
                result=result + word1[i]
            i=i+1

            


        return result
        