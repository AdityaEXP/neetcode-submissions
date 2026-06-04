# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answers = []
        def dfs(root, max_value=float("-inf")):
            nonlocal answers

            if not root:
                return -1

            max_value = max(root.val, max_value)
            left, right = dfs(root.left, max_value), dfs(root.right, max_value)

            if left == -1 or right == -1:
                if root.val >= max_value:
                    answers.append(root.val)

            return -1

        # answers.append(root.val) mistake, i then found out its auto included in recursion
        dfs(root)

        print(answers)

        return len(answers)



