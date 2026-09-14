class Solution(object):
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)

        while left <= right:

            mid = (left + right) // 2

            total_hours = 0

            for i in range(len(piles)):

                quo = piles[i] // mid
                rem = piles[i] % mid

                if rem > 0:
                    total_hours += quo + 1
                else:
                    total_hours += quo

            if total_hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left


        
        