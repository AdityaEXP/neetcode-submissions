class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depends = {}

        for a, b in prerequisites:
            if not a in depends:
                depends[a] = []
            if not b in depends:
                depends[b] = []

            depends[a].append(b)

        visited = set()

        def dfs(node, seen=None):
            if not seen:
                seen = set()

            if node in seen:
                # cycle detected
                return False

            if node in visited:
                # already studied this subject
                return True 

            if not depends[node]:
                # independent node
                visited.add(node)
                return True   

            seen.add(node)
            ans = []

            for x in depends[node]:
                ans.append(dfs(x, seen))

            seen.remove(node)

            return all(ans)

        print(depends)
        for node in depends:
            sucess = dfs(node)
            print(sucess, node, visited)
            if not sucess:
                return False

        return True