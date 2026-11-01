
class Solution(object):
    def strWithout3a3b(self, a, b):
        result = []

        while a > 0 or b > 0:
            if a > b:
                if a > 0 and not (len(result) >= 2 and result[-1] == 'a' and result[-2] == 'a'):
                    result.append('a')
                    a -= 1
                else:
                    result.append('b')
                    b -= 1
            else:
                if b > 0 and not (len(result) >= 2 and result[-1] == 'b' and result[-2] == 'b'):
                    result.append('b')
                    b -= 1
                else:
                    result.append('a')
                    a -= 1

        return ''.join(result)



        
        