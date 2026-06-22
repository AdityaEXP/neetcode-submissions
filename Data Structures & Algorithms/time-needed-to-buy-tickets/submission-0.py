class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([i for i in range(len(tickets))])

        hmap = {}
        for i, t in enumerate(tickets):
            hmap[i] = t

        time = 0
        while q:
            time+=1
            curr = q.popleft()
            hmap[curr] -= 1


            if hmap[curr] != 0:
                q.append(curr)
            else:
                if curr == k:
                    return time              
        

        