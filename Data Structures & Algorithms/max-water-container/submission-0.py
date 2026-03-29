class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        water=0
        for i in range(1,len(heights)):
            water=max(min(heights[l],heights[r])*(r-l),water)
            if heights[l]<=heights[r]:
                l=l+1
            else:
                r=r-1
        return water


        