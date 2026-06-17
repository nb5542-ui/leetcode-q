class Solution(object):
    def moveZeroes(self, nums):
        write = 0
        for read in range(len(nums)):
            if nums[read]!=0:
                nums[write] = nums[read]
                write +=1

        while write < len(nums):

            nums[write] = 0
            write += 1

                
        