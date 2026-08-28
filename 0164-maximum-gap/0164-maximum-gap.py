class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        max_num = 0

        for i in range(1,len(nums)):
            ans = nums[i] - nums[i-1]
            max_num = max(ans,max_num)

        return max_num

        





        


        
        