# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        max diameter path can be from any node.

        so we keep track of max_depth and at every node we do:

        max_dia = max(max_dia, left + right)
        """

        max_dia = 0

        def dfs(node):
            nonlocal max_dia
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            max_dia = max(max_dia, left + right)

            return 1 + max(left, right)

        dfs(root)

        return max_dia

        