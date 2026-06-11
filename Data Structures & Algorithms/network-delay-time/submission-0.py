class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adList = defaultdict(list)

        for u, v, w in times:
            adList[u].append((w, v))

        heap = []
        heap.append((0, k))

        shortest = {}

        while heap:
            w1, u = heapq.heappop(heap)

            if u in shortest:
                continue

            shortest[u] = w1 

            for w2, v in adList[u]:
                if v not in shortest:
                    heapq.heappush(heap, (w1 + w2, v))

        total_time = 0

        for i in range(1, n + 1):
            if i == k: continue 

            if not i in shortest:
                return -1

            total_time = max(total_time, shortest[i])

        return total_time
