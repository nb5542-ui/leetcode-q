class Solution(object):
    def subsets(self, nums):
        ans = []
        subset = []

        def dfs(index):
            if index == len(nums):
                ans.append(subset[:])
                return

            subset.append(nums[index])
            dfs(index + 1)

            subset.pop()

            dfs(index + 1)

        dfs(0)
        return ans
        