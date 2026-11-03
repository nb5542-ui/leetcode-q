class Solution(object):
    def minMoves(self, nums):
        ans = 0
        count = 0

        nums.sort(reverse = True)

        for i in range(len(nums)):
            ans = nums[0] - nums[i]

            count += ans

        return count




        
        