class Solution(object):
    def lastRemaining(self, n):
        if n == 1:
            return 1

        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))
        

        
        

        


        

        

        
         
        