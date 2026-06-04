"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return
    
        seen = {}
        q = deque()
        q.append(node)
        temp = Node(node.val)
        seen[temp.val] = temp

        while q:
            for i in range(len(q)):
                curr = q.popleft()

                if not curr.val in seen:
                    seen[curr.val] = Node(curr.val)

                for n in curr.neighbors:

                    if n.val not in seen:
                        seen[n.val] = Node(n.val)
                        q.append(n)

                    seen[curr.val].neighbors.append(seen[n.val])
                    

        return temp
            

                    

