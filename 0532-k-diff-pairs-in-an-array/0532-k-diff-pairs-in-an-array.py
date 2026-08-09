class Solution(object):
    def findPairs(self, nums, k):

        if k < 0:
            return 0

        
        if k == 0:
            freq = {}

            for x in nums:
                freq[x] = freq.get(x, 0) + 1

            count = 0

            for x in freq:
                if freq[x] > 1:
                    count += 1

            return count

        s = set(nums)
        count = 0

        for x in s:
            if x + k in s:
                count += 1

        return count