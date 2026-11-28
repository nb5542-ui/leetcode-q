
class Solution(object):
    def minimumTotal(self, triangle):

        n = len(triangle)
        memo = {}

        def solve(i, j):

            # Base condition
            if i == n - 1:
                return triangle[i][j]

            if (i,j) in memo:
                return memo[(i,j)]

            # Two possible paths
            left = solve(i + 1, j)
            right = solve(i + 1, j + 1)

            memo[(i,j)] = triangle[i][j] + min(left, right)

            # Current value + minimum path
            return memo[(i,j)]

        return solve(0, 0)


        
        