class Solution(object):
    def dominantIndex(self, nums):
        largest = -1
        second = -1
        largest_index = -1

        for i in range(len(nums)):
            if nums[i] > largest:
                second = largest
                largest = nums[i]
                largest_index = i

            elif nums[i] > second:
                second = nums[i]

        if largest >= 2 * second:
            return largest_index

        return -1


        

        