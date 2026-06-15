class Solution:
    def reverse(self, x: int) -> int:
        
        result = 0
        nums = abs(x)

        while nums > 0:
            result = (result * 10) + (nums % 10)
            nums = nums // 10

        if not (-2**31 <= result <= 2**31-1):
            return 0

        return result if x > 0 else -result