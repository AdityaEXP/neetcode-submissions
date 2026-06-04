class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        for i in range(n):
            stones[i]*=-1

        heapq.heapify(stones)

        while True:
            status = len(stones)

            if status == 0:
                return 0
            
            if status == 1:
                return abs(stones[-1])

            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))

            if x != y:
                heapq.heappush(stones, y - x)
        


