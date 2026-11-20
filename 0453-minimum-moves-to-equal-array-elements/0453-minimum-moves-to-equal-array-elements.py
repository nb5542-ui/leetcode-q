class Solution(object):
    def minMoves(self, nums):

        minimum = min(nums)

        ans = 0

        for i in range(len(nums)):

            ans += nums[i] - minimum

        return ans
        
        



