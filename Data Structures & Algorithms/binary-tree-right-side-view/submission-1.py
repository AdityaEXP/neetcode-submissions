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
            
            level = 0
            while len(queue) > 0:
                answer.append(queue[-1].val)
                for i in range(len(queue)):
                    curr = queue.popleft()
                    print(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level += 1

        bfs(root)
        return answer