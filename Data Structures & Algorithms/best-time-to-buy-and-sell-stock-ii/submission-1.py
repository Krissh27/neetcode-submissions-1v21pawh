class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum1=0
        mini=prices[0]
        for i in prices:
            if i<mini:
                mini=i
            else:
                sum1=sum1+i-mini
                mini=i
        return sum1