class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adList = defaultdict(list)

        for u, v, price in flights:
            adList[u].append((price, v))

        heap = [(0, -1, src)] # distance, k current, node
        shortest = {}
        best = {}

        best[(src, -1)] = 0

        min_price = float("inf")

        while heap:
            d1, stops, v = heapq.heappop(heap)

            if stops > k: continue
            # if (stops, v) in shortest: continue 

            if best.get((stops, v), float("inf")) < d1: continue

            if v == dst: min_price = min(min_price, d1)

            # shortest[(stops, v)] = d1 

            for d2, u in adList.get(v, []):
                new_price = d1 + d2 
                if new_price < best.get((stops + 1, u), float("inf")):
                    best[(stops + 1, u)] = new_price
                    heapq.heappush(
                        heap,
                        (d1 + d2, stops + 1, u)
                    )

        return min_price if min_price != float("inf") else -1