# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst=[]
        count=0
        for i in lists:
            if i:
                heapq.heappush(lst, [i.val,count,i])
                count+=1
        res=ListNode(0)
        head=res
        while lst:
            i,k,j=heapq.heappop(lst)
            res.next=ListNode(i)
            res=res.next
            if j.next==None:
                continue
            heapq.heappush(lst, [j.next.val,k,j.next])
        return head.next
            
        

        