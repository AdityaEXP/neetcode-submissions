class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        
        start, end = intervals[0]
        final = []
        for i in range(1, len(intervals)):
            s, e = intervals[i]

            if end >= s:
                end = max(end, e)
                start = min(start, s)            
            else:
                final.append([start, end])
                start, end = s, e

        final.append([start, end])

        return final