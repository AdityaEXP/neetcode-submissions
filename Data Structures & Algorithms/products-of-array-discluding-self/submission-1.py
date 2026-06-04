class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productSum = 1
        
        def returnZeroSum(indexZero):
            productSum = 1
            countZero = 0

            for x in nums:
                if x != 0:
                    productSum *= x
                else:
                    countZero+=1
            
            finalList = []

            if countZero > 1:
                for i in range(len(nums)):
                    finalList.append(0)
                return finalList

            for i in range(len(nums)):
                if i == indexZero:
                    finalList.append(int(productSum))
                else:
                    finalList.append(0)

            return finalList

        for i, value in enumerate(nums):
            productSum *= value
            if value == 0: return returnZeroSum(i)

        finalList = []

        for i, value in enumerate(nums):
            finalList.append(int(productSum/nums[i]))
        
        return finalList
