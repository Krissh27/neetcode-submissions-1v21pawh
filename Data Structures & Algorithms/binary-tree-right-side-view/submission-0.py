# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       
        self.list1=[]
        self.tavl=0
        def transverse(root):
            if root == None:
                return
            self.tavl+=1
       
            if len(self.list1)<self.tavl:
                self.list1.append(root.val)
            
            transverse(root.right)
            
            transverse(root.left)
            self.tavl-=1
            
            return 
        transverse(root)
        return self.list1






            


        