# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        sec=slow.next
        slow.next = None
        slow=sec

        while slow !=None:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        front = head
        back = prev
        while back:
            temp1 = front.next
            temp2 = back.next

            front.next = back
            back.next = temp1

            front = temp1
            back = temp2
            
            
            
      




        
        