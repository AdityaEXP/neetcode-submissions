class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adMap = {}

        for a, b in prerequisites:
            if not a in adMap:
                adMap[a] = []
            if not b in adMap:
                adMap[b] = []

            adMap[a].append(b)

        print(adMap)

        perma_visited = set()

        def dfs(i, state):
            if i in perma_visited:
                return True

            state.add(i)


            for nei in adMap[i]:

                if nei in state: 
                    return False
                
                if not dfs(nei, state):
                    return False
        
            state.remove(i)

            
            return True

            
        
        for subject in adMap:
            canFinish = dfs(subject, set())

            if not canFinish:
                return False
            
            perma_visited.add(subject)

        return True
