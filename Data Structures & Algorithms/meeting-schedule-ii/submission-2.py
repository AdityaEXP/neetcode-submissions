"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        temp = []
        for it in intervals:
            temp.append([it.start, it.end])

        temp.sort()

        total_rooms = 1
        

        heap =[temp[0][1]]

        for i in range(1, len(intervals)):
            s, e = temp[i]

            room_avail = s >= heap[0]

            if room_avail:
                heapq.heappop(heap)
            else:    
                total_rooms+=1

            heapq.heappush(heap, e)
            

        return total_rooms



        