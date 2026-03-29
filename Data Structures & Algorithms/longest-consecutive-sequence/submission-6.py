class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        li=set()
        for i in nums:
            li.add(i)
        count=0
        for i in nums:
            countt=0
            if i not in li:
                continue
            k=i
            while k-1 in li:
                k=k-1
            while k in li:
                li.remove(k)
                k=k+1
                countt+=1
            count=max(count,countt)
        return count


        