# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b>a:
                b,a=a,b
            while b!=0:
                a,b=b,a%b
            return a
        k=head
        while k.next:
            a,b=k.val,k.next.val
            g=gcd(a,b)
            temp=k.next
            k.next=ListNode(g,temp)
            k=temp
        return head



        