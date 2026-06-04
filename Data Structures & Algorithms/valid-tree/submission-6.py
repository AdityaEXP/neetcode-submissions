class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):

            visited.add(node)

            for nei in graph[node]:

                # Ignore the edge we came from
                if nei == parent:
                    continue

                # Already visited through another path -> cycle
                if nei in visited:
                    return False

                if not dfs(nei, node):
                    return False

            return True

        # Cycle check
        if not dfs(0, -1):
            return False

        # Connectivity check
        return len(visited) == n