class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adList = defaultdict(list)

        for u, v, price in flights:
            adList[u].append((price, v))

        heap = [(0, -1, src)] # distance, k current, node
        best = {}
        best[(src, -1)] = 0

        while heap:
            w1, k1, u = heapq.heappop(heap)

            if k1 > k: continue

            if best.get((u, k1), float("inf")) < w1: continue

            if u == dst: return w1


            for w2, v in adList[u]:
                new_price = w1 + w2 
                if new_price < best.get((v, k1 + 1), float("inf")):
                    heapq.heappush(heap, (w1 + w2, k1 + 1, v))

        return -1
