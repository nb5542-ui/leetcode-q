class Solution(object):
    def smallestIndex(self, nums):
        
        for i in range(len(nums)):
            
            num = nums[i]
            result = 0
            
            while num > 0:
                rem = num % 10
                result += rem
                num = num // 10
            
            if result == i:
                return i
        
        return -1


        
        