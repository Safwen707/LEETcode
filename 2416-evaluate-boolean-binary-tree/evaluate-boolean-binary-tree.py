# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs_recursive(root):
 
    if root.val==0:
        return False
    if root.val==1:
        return True
    
    if root.val==2:
        return (dfs_recursive(root.left) or dfs_recursive(root.right))
    if root.val==3:
        return (dfs_recursive(root.left) and dfs_recursive(root.right))



 
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return dfs_recursive(root)
        
        
        
        
        