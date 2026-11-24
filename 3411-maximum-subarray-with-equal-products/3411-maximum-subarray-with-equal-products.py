import math

class Solution(object):
    def maxLength(self, nums):

        ans = 0
        n = len(nums)

        for left in range(n):

            prod = 1
            g = 0
            l = 1

            for right in range(left, n):

                x = nums[right]

                prod *= x
                g = math.gcd(g, x)
                l = math.lcm(l, x)

                if prod == g * l:
                    ans = max(ans, right - left + 1)

        return ans