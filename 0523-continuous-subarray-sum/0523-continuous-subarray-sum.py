class Solution(object):
    def checkSubarraySum(self, nums, k):

        prefix = 0

        remainder_index = {0: -1}

        for i in range(len(nums)):

            prefix += nums[i]

            rem = prefix % k

            if rem in remainder_index:

                if i - remainder_index[rem] >= 2:
                    return True

            else:

                remainder_index[rem] = i

        return False
        