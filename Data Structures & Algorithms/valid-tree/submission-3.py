class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        a tree has all nodes connected, so exactly n - 1 edges,
        and no cycles

        also as this is directed graph, its not possible to maintain a visit recursion set() to track
        of the dfs.
        edges in cycle is greater than 1.

        so for each dfs call if 2nd last element of set is same as current node its just directed cycle we ignore,
        but if distance not 1 and node still in seen recursion set then cycle.
        """

        number_edges = len(edges)
        if not number_edges == n - 1:
            return False
        
        adList = {}

        for a, b in edges:
            if not a in adList: adList[a] = []
            if not b in adList: adList[b] = []

            adList[a].append(b)
            adList[b].append(a)

        for i in range(n):
            if not i in adList:
                adList[i] = []

        # done constructing adjacency List

        def dfs(node, parent, visited=None):
            if not visited:
                visited = set()

            visited.add(node)

            for n in adList[node]:
                if n == parent:
                    continue

                if n in visited and n != parent:
                    return False

                if not dfs(n, node, visited):
                    return False

            return True

        for node in adList:
            if not dfs(node, -1):
                return False

        return True
