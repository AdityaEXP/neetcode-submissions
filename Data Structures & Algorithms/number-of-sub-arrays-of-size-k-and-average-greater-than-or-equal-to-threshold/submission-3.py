class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        answer = 0
        currsum = sum(arr[0: k])

        l = 0

        if (currsum) / k >= threshold:
            answer+=1

        for r in range(k, len(arr)):
            currsum+=arr[r]
            currsum-=arr[l]
            l+=1
            if (currsum) / k >= threshold:
                answer+=1
            

        return answer