class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle = 0

        waiting = []

        task_dict = {}

        heap = []

        for t in tasks:
            task_dict[t] = task_dict.get(t, 0) - 1

        for key, value in task_dict.items():
            heapq.heappush(heap, (value, key))


        # 1 cycle required for 1 operation, so in one loop either task or waiting
        while heap or waiting:
        
            while waiting and waiting[0][0] < cycle:
                _, k = heapq.heappop(waiting)
                heapq.heappush(heap, (task_dict[k], k))

            
            if heap:
                f, k = heapq.heappop(heap)
                task_dict[k] += 1

                if f + 1 != 0:
                    heapq.heappush(waiting, (cycle+n, k))

            cycle+=1



        return cycle

