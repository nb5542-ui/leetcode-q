class Solution(object):
    def canJump(self, nums):
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False

            reachable = max(reachable, i + nums[i])

        return True
        
        