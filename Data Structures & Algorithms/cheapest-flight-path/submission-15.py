class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adList = defaultdict(list)

        for u, v, price in flights:
            adList[u].append((price, v))

        heap = [(0, -1, src)] # distance, k current, node
        shortest = {}

        while heap:
            w1, k1, u = heapq.heappop(heap)

            if k1 > k: continue 

            if u == dst:
                return w1

            shortest[u] = min(float("inf") if not u in shortest else shortest[u], w1)

            for w2, v in adList[u]:
                if v not in shortest:
                    heapq.heappush(heap, (w1 + w2, k1 + 1, v))

        return -1

