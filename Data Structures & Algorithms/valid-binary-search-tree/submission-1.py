# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val = []

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            val.append(root.val)
            inorder(root.right)

        inorder(root)

        i = 0
        print(val)
        for i in range(len(val) - 1):
            if not val[i] < val[i + 1]:
                return False

        return True
