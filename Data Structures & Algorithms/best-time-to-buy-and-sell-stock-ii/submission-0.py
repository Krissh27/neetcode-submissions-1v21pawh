class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        r,l=0,0
        while r<len(prices):
            if prices[r]-prices[l]>0:
                maxp=maxp+prices[r]-prices[l]
                l=r
                r=r+1
                
            else:
                l=r
                r=r+1
        return maxp


        