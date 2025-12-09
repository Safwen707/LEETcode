# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs_recursive(root):
    if not root:
        return []
    # pré-ordre : racine, gauche, droite
    return [root.val] + dfs_recursive(root.left) + dfs_recursive(root.right)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        l=dfs_recursive(root)
        if not root :
            return root
        if not root.left and not root.right:
            return root

        root.left=None
        curr=root
        k=TreeNode()
        for e in l[1:len(l)-1]:
            print (e)

            curr.right=TreeNode(e,None,k)
            print(curr.right)
            curr=curr.right
        curr.right=TreeNode(l[-1])



        
        return root



        """
        Do not return anything, modify root in-place instead.
        """
        