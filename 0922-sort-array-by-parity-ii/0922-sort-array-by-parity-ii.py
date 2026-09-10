class Solution(object):
    def sortArrayByParityII(self, nums):

        i = 0
        j = 1

        while i < len(nums):

            if nums[i] % 2 != 0:

                while nums[j] % 2 != 0:
                    j += 2

                nums[i], nums[j] = nums[j], nums[i]

                j += 2

            i += 2

        return nums
        