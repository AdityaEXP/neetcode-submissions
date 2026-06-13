"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        temp = []
        for it in intervals:
            temp.append([it.start, it.end])
        
        temp.sort()

        start, end = temp[0]


        for i in range(1, len(temp)):
            s, e = temp[i]

            if not s >= end:
                return False
            else:
                start, end = s, e 
        
        return True
