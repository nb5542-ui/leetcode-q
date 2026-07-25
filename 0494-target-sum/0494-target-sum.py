class Solution(object):
    def findTargetSumWays(self, nums, target):
        memo = {}
        def dfs(i,target):
            if i == len(nums):
                return 1 if target == 0 else 0

            if (i,target) in memo:
                return memo[(i,target)]

            plus = dfs(i + 1,target - nums[i])

            minus = dfs(i + 1,target + nums[i])

            memo[(i,target)] = plus + minus

            return memo[(i,target)]

        return dfs(0,target)
        