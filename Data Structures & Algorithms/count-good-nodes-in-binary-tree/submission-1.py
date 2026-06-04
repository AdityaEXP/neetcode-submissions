# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_value=float("-inf")):
            if not root:
                return 0

            good = 0

            if root.val >= max_value:
                good+=1

            max_value = max(max_value, root.val)

            return good + dfs(root.left, max_value) + dfs(root.right, max_value)

        return dfs(root)

