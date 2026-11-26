
class Solution(object):
    def canAliceWin(self, n):
        count = 0
        x = 10

        while n >= x:
            n -= x
            count += 1
            x -= 1

        return count % 2 == 1






        
        