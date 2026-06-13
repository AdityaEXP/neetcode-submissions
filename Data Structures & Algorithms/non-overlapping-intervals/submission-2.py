class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        start, end = intervals[0]
        total = 0

        for i in range(1, len(intervals)):
            s, e = intervals[i]

            # overlapping condition

            if (end > s):
                # keep small one and delete big one 
                total+=1

                if end > e:
                    start, end = s, e
                else:
                    start, end = start, end

            else:
                start, end = s, e
        
        return total
