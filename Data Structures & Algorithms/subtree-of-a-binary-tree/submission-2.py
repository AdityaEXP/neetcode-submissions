class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        valid_answers = []

        def isSameTree(p, q):
            def dfs(p, q):
                if not p and not q:
                    return True

                if not p or not q:
                    return False

                if not p.val == q.val:
                    return False

                return dfs(p.left, q.left) and dfs(p.right, q.right)

            return dfs(p, q)
        
        def dfs(root):
            nonlocal valid_answers
            if not root:
                return False

            if root.val == subRoot.val:
                valid_answers.append(root)

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        founded = valid_answers

        if not founded:
            return False

        for f in founded:
            if isSameTree(subRoot, f):
                return True

        return False