class Solution:
    def longestEqualSubarray(self, nums, k):
        freq = {}
        left = 0
        max_freq = 0
        answer = 0

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            max_freq = max(max_freq, freq[nums[right]])

            while (right - left + 1) - max_freq > k:
                freq[nums[left]] -= 1
                left += 1

            answer = max(answer, max_freq)

        return answer