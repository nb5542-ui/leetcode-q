
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        # Find the smallest feasible difference level
        while left < right:
            mid = (left + right) // 2
            needed = sum(max(d - mid, 0) for d in diffs)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        remaining = k - sum(max(d - level, 0) for d in diffs)

        ans = 0

        for d in diffs:
            d = min(d, level)

            if remaining > 0 and d == level and d > 0:
                d -= 1
                remaining -= 1

            ans += d * d

        return ans





        





        
        