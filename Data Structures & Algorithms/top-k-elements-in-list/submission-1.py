class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}

        for x in nums:
            if x in seen:
                seen[x] += 1
            else:
                seen[x] = 1

        print(seen)
        bucket = [[] for _ in range(len(nums) + 1)]
        print(bucket)
        for ele, frequency in seen.items():
            print(ele, frequency)
            bucket[frequency].append(ele)
        print(bucket)

        
        result = []
        for i in range(len(bucket) - 1, -1, -1):
            if len(result) == k: break

            for ex in bucket[i]:
                result.append(ex)

        return result


        