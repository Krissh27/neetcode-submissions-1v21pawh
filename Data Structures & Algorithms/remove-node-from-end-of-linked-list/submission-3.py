# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return head
        if head.next==None:
            head=None
            
            return head
        rizz1=head
        for i in range(n):

            rizz1=rizz1.next
        if rizz1 is None:
            return head.next

        rizz2=head
        temp=head
        while rizz1 is not None:
            rizz1=rizz1.next
            
            temp=rizz2
            rizz2=rizz2.next
        
        temp.next=temp.next.next
        rizz2.next=None
        return head


