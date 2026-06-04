# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        answer = None

        def dfs(root):
            nonlocal count
            nonlocal answer

            if not root:
                return

            dfs(root.left)
            if count == k:
                answer = root.val
            count+=1
            
            dfs(root.right)
        
        dfs(root)

        return answer

    


