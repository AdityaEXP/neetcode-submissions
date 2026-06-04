class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adList = {}

        for a, b in prerequisites:
            if not a in adList: adList[a] = []
            if not b in adList: adList[b] = []

            adList[a].append(b)

        for i in range(numCourses):
            if not i in adList:
                adList[i] = []

        visited = []

        def dfs(node, seen=None):
            if not seen:
                seen = set()

            if node in seen:
                # cycle detected
                return False
            
            if node in visited:
                # this chain already has sucess
                return True

            if not adList[node]:
                # independent subject chain completed
                # but make sure to add it to visited
                visited.append(node)
                return True

            seen.add(node)

            for n in adList[node]:
                if not dfs(n, seen):
                    return False

            seen.remove(node)
            visited.append(node)


            return True

        for n in adList:
            if not dfs(n):
                return []

        return visited


