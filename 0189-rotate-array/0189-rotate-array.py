class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k%n

        ans = []
        for i in range(n-k,n):
            ans.append(nums[i])

        for i in range(0,n-k):
            ans.append(nums[i])

        nums[:] = ans
        

        
        
        