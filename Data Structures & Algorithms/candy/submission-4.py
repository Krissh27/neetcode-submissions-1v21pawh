class Solution:
    def candy(self, ratings: List[int]) -> int:
        resultl=[1]*len(ratings)
        resultr=[1]*len(ratings)
        n=len(ratings)
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                resultl[i]=resultl[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                resultr[i]=resultr[i+1]+1
        count=0
        for i in range(n):
            count+=max(resultr[i],resultl[i])
        return count

        