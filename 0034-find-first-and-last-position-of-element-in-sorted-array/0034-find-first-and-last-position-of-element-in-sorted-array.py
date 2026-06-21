class Solution(object):
    def searchRange(self, nums, target):

        def findFirst():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    ans = mid
                    right = mid - 1

            return ans

        def findLast():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    ans = mid
                    left = mid + 1

            return ans

        return [findFirst(), findLast()]
        