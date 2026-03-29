class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr=0
        rr=len(matrix)-1
        mid=(lr+rr)//2
        while lr<=rr:
            if matrix[mid][0]>target:
                rr=mid-1
            elif matrix[mid][-1]<target:
                lr=mid+1
            elif matrix[mid][0]<=target<=matrix[mid][-1]:
                l,r=0,len(matrix[mid])-1
                while l<=r:
                    mid2= (l+r)//2
                    if matrix[mid][mid2]>target:
                        r=mid2-1
                    elif matrix[mid][mid2]<target:
                        l=mid2+1
                    elif matrix[mid][mid2]==target:
                        return True 
                    mid2= (l+r)//2 
                      
                return False 
            mid=(lr+rr)//2
        return False
        

            

        