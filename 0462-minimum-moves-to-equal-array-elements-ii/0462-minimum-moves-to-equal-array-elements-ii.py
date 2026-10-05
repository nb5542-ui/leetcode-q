class Solution(object):
    def minMoves2(self, nums):
        ans = 0
        
        mid = len(nums)//2

        nums.sort()
        for i in range(len(nums)):

            ans += abs(nums[mid]-nums[i])

        return ans



        
        