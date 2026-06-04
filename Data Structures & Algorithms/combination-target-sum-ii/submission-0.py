class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        whenever their was duplicate in backtracking problem, i remeber we sorted the array
        cause it makes duplicates handling easier, as the next recursion level will contain new duplicate number

        so we dont need to check via membership operation if duplicate already there and we will also dont know
        if its the same. dont know its confusing maybe my concept here weak.

        so basically if we sorted the array. after that we start dfs, take first element take second and soo on
        i guess. same thing base case if sum of array > target or index of bound.

        EDIT: ohh i see by sorting and i+1 condition we skip duplicate problem, i kinda remebered the template
        even after months.
        """
        candidates.sort()
        answers = []
        n = len(candidates)

        def dfs(index, subset, curr_sum):            
            if curr_sum == target:
                answers.append(subset[:])
                return
            
            if curr_sum > target:
                return
            
            if index >= n:
                return
            
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                dfs(i+1, subset, curr_sum+candidates[i])
                subset.pop()

        dfs(0, [], 0)
        return answers
