# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        n1=l1
        n2=l2
        dummy=ListNode(-1)
        curr=dummy
        while n1 or n2 or carry:
            if not n1:
                z1=0
            else:
                z1=n1.val
            if not n2:
                z2=0
            else:

            
                z2=n2.val
            val=z1+z2+carry
            carry=val//10
            val=val%10
            curr.next=ListNode(val)
            curr=curr.next
            if n1!=None:
                n1=n1.next
            if n2!=None:
                n2=n2.next
        return dummy.next



            

            
        