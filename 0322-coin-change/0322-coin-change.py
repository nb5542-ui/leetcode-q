class Solution(object):
    def coinChange(self, coins, amount):
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0

            if amount  < 0:
                return float("inf")

            if amount in memo:
                return memo[amount]

            answer = float("inf")
            for coin in coins:
                candidate = 1 + dfs(amount - coin)

                answer = min(answer,candidate)
            memo[amount] = answer
            return answer

        ans = dfs(amount)

        return ans if ans != float("inf") else -1


             
            
            
            
       
        

        