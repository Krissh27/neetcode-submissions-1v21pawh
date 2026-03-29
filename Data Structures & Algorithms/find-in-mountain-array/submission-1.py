class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        if mountainArr.length()<3:
            return -1
        l=1
        r=mountainArr.length() - 2
        mid=l+(r-l)//2
        while l<=r:
            
            if mountainArr.get(mid-1)<mountainArr.get(mid)>mountainArr.get(mid+1):
                break
            elif mountainArr.get(mid-1)<mountainArr.get(mid)<mountainArr.get(mid+1):
                l=mid+1
            else:
                r=mid-1
            mid=l+(r-l)//2

        peak=mid
        l=0
        r=mid
        while l<=r:
            mid=(l+r)//2
            if mountainArr.get(mid)<target:
                l=mid+1
            elif mountainArr.get(mid)>target:
                r=mid-1
            elif mountainArr.get(mid)==target:
                return mid



        mid=peak
        l=mid+1
        r=mountainArr.length()- 1
        while l<=r:
            mid=(l+r)//2
            if mountainArr.get(mid)<target:
                
                r=mid-1
            elif mountainArr.get(mid)>target:
                l=mid+1
            elif mountainArr.get(mid)==target:
                return mid
        return -1

                
        
        
            

        
        