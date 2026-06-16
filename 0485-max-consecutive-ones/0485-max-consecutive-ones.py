class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current = 0 
        maxi = 0
        for num in nums:
            if num == 1:
                current += 1
                maxi = max(current,maxi)
            else:
                current = 0

        return maxi
        
        