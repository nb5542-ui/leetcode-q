class Solution(object):
    def sortedSquares(self, nums):
        result = []
        
        for i in range(len(nums)):
            ans = nums[i]**2
            result.append(ans)

        return sorted(result)
        
        
        