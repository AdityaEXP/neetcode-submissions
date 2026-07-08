class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        State: f(i) -> max amount of money we can rob till ith house included.

        Meaning: as it as state 

        Why is the state sufficient? cause if we are at ith house there are only two possible choices
        1. rob current house and skip previous.
        2. skip current rob previous 

        Choices: f(i) = max(
            nums[i] + f(i - 2), # rob current 
            f(i - 1) # skip current 
        )

        Transition: wahts diff bw transition and chocies 

        Base case: n == 0, max money we can rob is nums[0]
        or n < 0 return 0

        Memoization validity: at certain index i we only need to know how much money we can make from 
        i - 1 house and i - 2 house path does not matter. 

        Time: not sure how to calculate on this one 

        Space: same not sure 

        Can the state be compressed?
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        memo = {}

        def f(i):
            if i in memo: return memo[i]

            if i == 0: return nums[0]
            if i < 0: return 0

            memo[i] = max(
                nums[i] + f(i - 2),
                f(i - 1)
            )

            return memo[i]

        return f(n - 1)

        