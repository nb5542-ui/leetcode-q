class Solution:
    def majorityElement(self, nums):

        freq = {}

        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ans = []

        n = len(nums)

        
        for num, count in freq.items():
            if count > n // 3:
                ans.append(num)

        return ans
            
        
        


        
        