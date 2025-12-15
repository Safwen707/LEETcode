# Time limiot exeeded
# Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# def dfs_recursive(root):
#     if not root:
#         return []
#     # pré-ordre : racine, gauche, droite
#     return [root] + dfs_recursive(root.left) + dfs_recursive(root.right)
# def hauteur(root) :
#     if not root :
#         return 0

#     return 1+max(hauteur(root.right),hauteur(root.left))



# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         dfs=dfs_recursive(root)
#         print(dfs)
#         l=[]
        
#         for root in dfs:
#             l.append(hauteur(root.right)+hauteur(root.left))
#         print(l)   
#         return max(l)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # variable globale pour stocker le diamètre maximum

        def height(node):
            if not node:
                return 0
            # hauteur des sous-arbres gauche et droit
            left_height = height(node.left)
            right_height = height(node.right)
            
            # mettre à jour le diamètre local
            self.diameter = max(self.diameter, left_height + right_height)
            
            # retourner la hauteur pour le parent
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter





        
        