class Solution(object):
    def findNthDigit(self, n):
        digits = 1
        start = 1
        while n > 9*start*digits:
            n -= 9*start*digits

            start *=10
            digits += 1

        number = start + (n-1)//digits
        index = (n-1)%digits

        return int(str(number)[index]) 



        
            
        
        

        