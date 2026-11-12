class Solution(object):
    def maxTurbulenceSize(self, arr):

        left = 0
        max_tur = 1

        for right in range(1, len(arr)):

            if arr[right] == arr[right - 1]:
                left = right

            elif right > 1 and (
                (arr[right] > arr[right - 1] and
                 arr[right - 1] > arr[right - 2]) or

                (arr[right] < arr[right - 1] and
                 arr[right - 1] < arr[right - 2])
            ):
                left = right - 1

            max_tur = max(max_tur, right - left + 1)

        return max_tur





            



        
        