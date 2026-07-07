class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        n = len(accounts)

        name_map = {}

        for i in range(n):
            acc = accounts[i]
            n1 = len(acc)
            name = acc[0]

            for v1 in range(1, n1):
                for v2 in range(1, n1):
                    if not acc[v1] in graph: graph[acc[v1]] = []
                    if not acc[v2] in graph: graph[acc[v2]] = []
                    name_map[acc[v1]] = name
                    name_map[acc[v2]] = name
                    if v1 == v2: continue                     

                    graph[acc[v1]].append(acc[v2])

        perma = set()
        def dfs(node, res):
            if node in perma: return
            
            res.append(node)
            perma.add(node)

            for nei in graph[node]:
                dfs(nei, res)

            return res

        ans = []

        for node in graph:
            if node in perma: continue
            all_emails = dfs(node, [])
            all_emails.sort()
            ans.append(
                [name_map[all_emails[0]], *all_emails]
            )
        return ans