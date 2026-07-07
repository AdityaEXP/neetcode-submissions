class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        n = len(accounts)

        name_map = {}

        for i in range(n):
            acc = accounts[i]
            n1 = len(acc)
            name = acc[0]

            for j in range(1, n1):
                name_map[acc[j]] = name 

            first = acc[1]

            for email in acc[1:]:
                if not email in graph: graph[email] = []
                graph[first].append(email)
                graph[email].append(first)

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