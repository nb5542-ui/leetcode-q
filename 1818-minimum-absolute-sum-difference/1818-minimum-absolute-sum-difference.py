import bisect

class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):

        MOD = 10**9 + 7

        sorted_nums = sorted(nums1)

        total = 0
        max_gain = 0

        for i in range(len(nums1)):

            old_diff = abs(nums1[i] - nums2[i])

            total += old_diff

            pos = bisect.bisect_left(sorted_nums, nums2[i])

            new_diff = old_diff

            if pos < len(sorted_nums):
                new_diff = min(new_diff, abs(sorted_nums[pos] - nums2[i]))

            if pos > 0:
                new_diff = min(new_diff, abs(sorted_nums[pos-1] - nums2[i]))

            gain = old_diff - new_diff

            max_gain = max(max_gain, gain)

        return (total - max_gain) % MOD

            





        

        





            


        