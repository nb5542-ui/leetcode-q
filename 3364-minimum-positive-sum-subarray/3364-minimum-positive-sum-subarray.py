class Solution(object):
    def minimumSumSubarray(self, nums, l, r):

        min_sum = float('inf')

        for i in range(len(nums)):

            curr_sum = 0

            for j in range(i, min(i + r, len(nums))):

                curr_sum += nums[j]

                length = j - i + 1

                if l <= length <= r and curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)

        if min_sum == float('inf'):
            return -1

        return min_sum



        




