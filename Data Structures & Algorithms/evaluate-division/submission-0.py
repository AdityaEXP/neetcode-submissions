class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)

        for i in range(n):
            a, b = equations[i]
            weight = values[i]
            graph[a].append((weight, b))
            graph[b].append((1/weight, a))

        
        def query(src, destination, visit, curr_value):
            if not src in graph or not destination in graph: return -1
            if src == destination: return curr_value
            if src in visit: return -1
            if not graph[src]: return -1


            visit.add(src)
            for w, nei in graph[src]:
                ans = query(nei, destination, visit, curr_value * w) 
                if not ans == -1:
                    return ans

            visit.remove(src)
            return -1

        # print(query("a", "c", set(), 1))
        # print(graph)

        queries = [query(x[0], x[1], set(), 1) for x in queries]
        return queries