# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(root1,root2):
    result=TreeNode()
    if not root1:
        return root2
    if not root2:
        return root1
    if not root1 and not root2 :
        return None
    result.val=root1.val+root2.val
    result.left=dfs(root1.left,root2.left)
    result.right=dfs(root1.right,root2.right)
    return result

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return dfs(root1,root2)


    
        