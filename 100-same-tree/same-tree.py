# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def bfsModified(root):
    if not root:
        return []

    queue = deque([root])
    

    result = []

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            else:
                queue.append(None)
            if node.right:
                queue.append(node.right)
            else:
                queue.append(None)
        else:
            result.append(None)

    return result

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print(bfsModified(p))
        print(bfsModified(q))
        return bfsModified(p)==bfsModified(q)
            
        