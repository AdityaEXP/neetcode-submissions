class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adList = defaultdict(list)

        for u, v, price in flights:
            adList[u].append((price, v))

        heap = [(0, -1, src)] # distance, k current, node
        shortest = {}

        while heap:
            w1, k1, u = heapq.heappop(heap)

            if k1 > k:
                continue

            if (u, k1) in shortest:
                continue

            shortest[(u, k1)] = w1

            for w2, v in adList[u]:
                heapq.heappush(heap, (w1 + w2, k1 + 1, v))

        all_possible = []

        for key, value in shortest.items():
            stop, k_used = key 
            cost = value 

            if k_used > k: continue
            if stop == dst:
                all_possible.append(cost)

        return min(all_possible) if all_possible else -1

