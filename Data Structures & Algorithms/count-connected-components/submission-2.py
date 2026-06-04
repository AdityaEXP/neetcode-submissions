class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        I am thinking of building an adList.

        then start dfs one by one, and if the node is not in permanent visited we increase count by 1.
        """

        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        permanent_visited = set()

        def dfs(node, parent):

            permanent_visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue

                if nei in permanent_visited:
                    continue

                dfs(nei, node)

        total_entitiy = 0

        for n in graph:
            if not n in permanent_visited:
                total_entitiy+=1
                dfs(n, -1)

        return total_entitiy



