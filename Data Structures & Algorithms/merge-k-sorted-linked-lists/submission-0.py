# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for li in lists:
            head = li 

            while head:
                heapq.heappush(heap, head.val)
                head = head.next 

        dummy = ListNode()
        temp = dummy


        while heap:
            val = heapq.heappop(heap)
            temp.next = ListNode(val)
            temp = temp.next 

        return dummy.next