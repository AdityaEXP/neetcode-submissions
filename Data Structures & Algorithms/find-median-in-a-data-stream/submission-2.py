class MedianFinder:

    def __init__(self):
        self.LHeap = []
        self.RHeap = []

    def addNum(self, num: int) -> None:
        # invariant 1, size diff bw LHeap & RHeap <= 1
        # invariant 2, each element of LHeap < each element of RHeap
        # So my conclusion is we will also need some kind of temp memory
        # part1: also i think we need to transfer max element of left heap
        # part2: and min element of right heap should be exchange in bw when balance is disturbed

        # if not self.LHeap:
        #     heapq.heappush(self.LHeap, -num)
        #     return
        
        heapq.heappush(self.LHeap, -num)
        heapq.heappush(
            self.RHeap,
            -heapq.heappop(self.LHeap)
        )
        size_left, size_right = len(self.LHeap), len(self.RHeap)

        if size_right > size_left:
            heapq.heappush(
                self.LHeap,
                -heapq.heappop(self.RHeap)
            )
        

    def findMedian(self) -> float:
        size_left, size_right = len(self.LHeap), len(self.RHeap)

        # if size equal median is average of both (absolute value average afcourse)

        if size_left == size_right:
            answer = ( -self.LHeap[0] + self.RHeap[0] ) / 2
            return answer  

        return -self.LHeap[0]
        