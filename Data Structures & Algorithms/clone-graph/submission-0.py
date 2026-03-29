"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return None
        queue = deque([node])
        clones = {node: Node(node.val)}
        seen=set()
        
        while queue:
            kk=queue.popleft()
            for i in kk.neighbors:
                if i not in clones:
                    clones[i]=Node(i.val)
                    queue.append(i)
                clones[kk].neighbors.append(clones[i])
                
        return clones[node]
        
        
        
        
        

            


        