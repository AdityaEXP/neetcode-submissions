class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        I am thinking of building an adList.

        start dfs on node which is not in permanent_visited and increase count by 1.

        in dfs we basically add it in permanent_visited then apply dfs on neighbour, we can detect parent 
        easily and continue in that case, i think i can just use the permanent_visited to beign with no parent case.
        """

        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        permanent_visited = set()

        def dfs(node):

            permanent_visited.add(node)

            for nei in graph[node]:

                if nei in permanent_visited:
                    continue

                dfs(nei)

        total_entitiy = 0

        for n in graph:
            if not n in permanent_visited:
                total_entitiy+=1
                dfs(n)

        return total_entitiy



