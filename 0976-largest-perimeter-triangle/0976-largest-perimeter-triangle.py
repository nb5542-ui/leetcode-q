class Solution(object):
    def largestPerimeter(self, nums):
        max_peri = 0
        nums.sort()

        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                peri = nums[i]+nums[i+1]+nums[i+2]

                max_peri = max(max_peri,peri)

        return max_peri   
        
            


        
        