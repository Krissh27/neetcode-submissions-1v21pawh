class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[0]*(n+1)
        for i in range(n+1):
            for j in range(31):
                if i&(1<<j):
                    arr[i]+=1
        return arr
        