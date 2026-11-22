class Solution(object):
    def checkString(self, s):
        seen_b = False

        for ch in s:
            
            if ch == 'b':

                seen_b = True

            elif ch == 'a' and seen_b:
                return False

        return True


        




        
        