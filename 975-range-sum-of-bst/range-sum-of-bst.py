# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(root):
    if not root:
        return []
    # pré-ordre : racine, gauche, droite
    return   dfs(root.left)+[root.val] + dfs(root.right)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        numbers=dfs(root)
        print(numbers)
        l=[k for k in numbers if k in range(low,high+1)]
        return sum(l)

        