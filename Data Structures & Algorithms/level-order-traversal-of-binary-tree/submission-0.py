# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)

        answer = []

        while q:
            temp = []

            for i in range(len(q)):
                a = q.popleft()
                temp.append(a.val)

                if a.left:
                    q.append(a.left)
                
                if a.right:
                    q.append(a.right)

            answer.append(temp)

        return answer