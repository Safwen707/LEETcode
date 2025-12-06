def dfs(root, low, high):
    if not root:
        return 0

    if root.val < low:
        return dfs(root.right, low, high)   

    if root.val > high:
        return dfs(root.left, low, high)    

    # dans l'intervalle
    return root.val + dfs(root.left, low, high) + dfs(root.right, low, high)


class Solution:
    def rangeSumBST(self, root, low, high):
        return dfs(root, low, high)
