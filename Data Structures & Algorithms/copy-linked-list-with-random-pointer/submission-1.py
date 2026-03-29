"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        t=head
        while t !=None:
            nn=Node(t.val,t.next)
            t.next=nn
            t=nn.next
        t=head
        

        while t !=None:
            n=t.next
            
            if t.random:
                n.random=t.random.next
            t=t.next.next
        t=head
        kk=head.next
        while t !=None:
            copy=t.next
            t.next=copy.next
            if copy.next:
                copy.next=copy.next.next
            
            t=t.next
        return kk

        
            
        
            


            
           
        

        






        