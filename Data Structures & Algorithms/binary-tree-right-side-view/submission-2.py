# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rightSideView(self, root: Optional [TreeNode]) -> List[int]:
        answer = []
        
        def bfs(root):
            queue = deque()

            if root:
                queue.append(root)
            
            while queue:
                answer.append(queue[-1].val)
                for i in range(len(queue)):
                    a = queue.popleft()

                    if a.left:
                        queue.append(a.left)

                    if a.right:
                        queue.append(a.right)

        bfs(root)
        return answer