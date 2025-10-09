class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        winStart = 0
        winSum = 0
        results = []

        for i in range(0, len(nums)):
            winSum += nums[i]

            if(i>=k-1):
                results.append(winSum/k)
                winSum = winSum - nums[winStart]
                winStart += 1
        return max(results)        
        