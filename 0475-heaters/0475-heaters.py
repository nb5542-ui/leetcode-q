class Solution(object):
    def findRadius(self, houses, heaters):

        houses.sort()
        heaters.sort()

        j = 0
        radius = 0

        for house in houses:

            
            while j < len(heaters) - 1 and \
                  abs(house - heaters[j]) >= abs(house - heaters[j + 1]):
                j += 1

           
            distance = abs(house - heaters[j])

            
            radius = max(radius, distance)

        return radius