class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Graph type? undirected

        Question basically asking to find last edge which creates cycle in graph.

        what happens if i add an edge?
        if i add an edge [a, b] it creates a connection bw node a and b.

        How do I know an edge [a, b] creates a cycle? 
        ex: [[1,2],[1,3],[3,4],[2,4]]

        while constructing adjaceny list i wil call dfs(a, parent) same logic as course scheudle II
        on each edge and if cycle detected then that it is.

        but im unable to think about permanent state here, what should i cache?
        """

        

        adMap = {}

        def dfs(a, b, parent, state):
            
            state.add(a)

            for nei in adMap[a]:
                
                if nei == b:
                    return True 

                if nei in state and nei == parent:
                    continue

                if dfs(nei, b, a, state):
                    return True
            
            state.remove(a)
            return False

        for a, b in edges:
            if not a in adMap:
                adMap[a] = []
            if not b in adMap:
                adMap[b] = []

            if dfs(a, b, -1, set()):
                return [a, b]
            
            adMap[a].append(b)
            adMap[b].append(a)
        


