# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        old=dummy
     
        kj=dummy.next
        while True:
            
            if kj!=None:
                curr=kj
                nex=curr.next

            for i in range(k):
                if kj==None:
                    return dummy.next
                kj=kj.next
            
            prev=kj

            for i in range(k):
                nex=curr.next
                curr.next=prev
                prev=curr
                curr=nex
                
            temp=old.next
            old.next=prev
            old=temp

            

            
            
            
            


            
            
        
            
                
            
            

                



        