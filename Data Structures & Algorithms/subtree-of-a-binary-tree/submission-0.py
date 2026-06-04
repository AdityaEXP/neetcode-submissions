class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isElementSame(subRoot1, subRoot2):
            if not subRoot1 and not subRoot2:
                return True
            if not subRoot1 or not subRoot2:
                return False

            if subRoot1.val != subRoot2.val:
                return False

            return isElementSame(subRoot1.left, subRoot2.left) and isElementSame(subRoot1.right, subRoot2.right)

        if not root:
            return False
        
        if isElementSame(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)