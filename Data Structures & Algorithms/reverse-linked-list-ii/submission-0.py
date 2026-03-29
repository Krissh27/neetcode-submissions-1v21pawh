
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        head =dummy
        Node1=head
        prev=None
        for i in range(left):
            prev=Node1
            Node1=Node1.next
        prev2=None

        for i in range(right-left+1):
            temp=Node1.next
            Node1.next=prev2
            prev2=Node1
            Node1=temp
        prev.next.next=Node1
        prev.next=prev2
        return head.next


        



