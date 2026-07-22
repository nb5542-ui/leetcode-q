class Solution(object):
    def permute(self, nums):

        ans = []
        curr = []
        used = [False]*len(nums)

        def dfs():
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                curr.append(nums[i])

                dfs()
                curr.pop()
                used[i] = False

        dfs()
        return ans
        
        
        