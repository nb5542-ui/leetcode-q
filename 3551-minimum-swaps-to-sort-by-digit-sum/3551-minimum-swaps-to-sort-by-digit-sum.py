
class Solution(object):
    def minSwaps(self, nums):
        def digitSum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        n = len(nums)

        # Original indices in the required sorted order
        order = sorted(
            range(n),
            key=lambda i: (digitSum(nums[i]), nums[i])
        )

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                j = order[j]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps

                    
               

                
        
            
        