class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        """
        so basically we need to merge intervals.

        ex: first [1, 3] and [1, 5]
        start same and end will be max(3, 5)

        ex: [1, 3] and [2, 3]
        start = min(1, 2) and end sam 

        ex: [1, 5] and [2, 10]
        start = min(1, 2) and end = max(5, 10)

        all these 3 cases only when start 2 <= end 1

        else seprate intervals.

        """

        intervals.sort()
        
        start, end = intervals[0]
        temp = []

        for s, e in intervals[1:]:
            if s <= end:
                end = max(end , e)
            else:
                temp.append([start, end])
                start, end = s, e 

        temp.append([start, end])
        
        return temp
            