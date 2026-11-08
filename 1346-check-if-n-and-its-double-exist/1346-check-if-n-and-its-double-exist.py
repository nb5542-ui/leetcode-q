class Solution(object):
    def checkIfExist(self, arr):

        arr.sort()

        for i in range(len(arr)):

            target = 2 * arr[i]

            left = 0
            right = len(arr) - 1

            while left <= right:

                mid = (left + right) // 2

                if arr[mid] == target:

                    if mid != i:
                        return True

                    else:
                        
                        left = mid + 1

                elif arr[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

        return False


            




        
        
        