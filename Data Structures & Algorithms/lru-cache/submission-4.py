class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dummyh= Node(-1,-1)
        self.dummyt= Node(-1,-1)
        self.dummyh.next=self.dummyt
        self.dummyh.prev=self.dummyh

        self.length=capacity
        self.ma=dict()

        

    def get(self, key: int) -> int:
        if key  not in self.ma:
            return -1
        nn= self.ma[key]
        nn.prev.next=nn.next
        nn.next.prev=nn.prev
        nn.next=self.dummyh.next
        nn.next.prev=nn
        self.dummyh.next=nn
        nn.prev=self.dummyh
        return nn.val


        

    def put(self, key: int, value: int) -> None:
        if key in self.ma:
            nn=self.ma[key]
            nn.val=value
            nn.prev.next=nn.next
            nn.next.prev=nn.prev
            nn.next=self.dummyh.next
            nn.next.prev=nn
            self.dummyh.next=nn
            nn.prev=self.dummyh
            return 





        if len(self.ma)<self.length:
            nn=Node(key,value)
            self.ma[key]=nn
            nn.next=self.dummyh.next
            nn.prev=self.dummyh
            self.dummyh.next=nn
            nn.next.prev=nn
            return
        pn=self.dummyt.prev
        pn.prev.next=pn.next
        pn.next.prev=pn.prev
        pn.next=pn.prev=None
        self.ma.pop(pn.key)
        nn=Node(key,value)
        self.ma[key]=nn
        nn.next=self.dummyh.next
        nn.prev=self.dummyh
        self.dummyh.next=nn
        nn.next.prev=nn
        return

        





        
