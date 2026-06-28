class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adList = defaultdict(list)

        for u, v, w in times:
            adList[u].append((w, v))

        heap = []
        heap.append((0, k))

        shortest = {}

        while heap:
            t1, u = heapq.heappop(heap)

            if u in shortest: continue 

            shortest[u] = t1 

            for t2, v in adList.get(u, []):
                heapq.heappush(
                    heap,
                    (t1 + t2, v)
                )

        if len(shortest) != n:
            return -1

        return max(shortest.values())