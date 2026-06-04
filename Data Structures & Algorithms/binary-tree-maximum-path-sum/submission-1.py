# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path = float("-inf")

        def dfs(root):
            nonlocal max_path

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            max_path = max(
                max_path,
                root.val + max(0, left) + max(0, right)
            )

            return root.val + max(0, left, right)

        dfs(root)

        return max_path
