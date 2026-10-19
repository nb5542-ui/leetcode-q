
class Solution(object):
    def targetIndices(self, nums, target):
        result = []
        nums.sort()

        for i in range(len(nums)):
            if target == nums[i]:
                result.append(i)

        return result

        
        