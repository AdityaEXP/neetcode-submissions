class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        all_elements = []
        for x in matrix:
            # print(x)
            all_elements = all_elements + x

        l, r = 0, len(all_elements) - 1

        # print(all_elements)
        while l <=r:
            mid = (l + r) // 2

            if target == all_elements[mid]:
                return True
            
            if target > all_elements[mid]:
                l = mid + 1

            if target < all_elements[mid]:
                r = mid - 1
        
        return False