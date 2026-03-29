# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        
        while len(q1)>0 or len(q2)>0:
            nodeq=q1.popleft()
            nodeq2=q2.popleft()
            if nodeq:
                q1.append(nodeq.left)
                q1.append(nodeq.right)
            if nodeq2:
                q2.append(nodeq2.left)
                q2.append(nodeq2.right)
            

            if nodeq==None and nodeq2==None:
                continue
            if (nodeq==None and  nodeq2!=None) or(nodeq2==None and  nodeq!=None):
                return False
            if nodeq.val==nodeq2.val:
                continue
            return False
        return True


            