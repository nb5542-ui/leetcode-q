
class Solution(object):
    def myAtoi(self, s):
        result = 0
        sign = 1
        s = s.strip()

        if not s:
            return 0

        i = 0

        if s[i] == '-':
            sign = -1
            i += 1

        elif s[i] == '+':
            sign = 1
            i += 1

        while i < len(s):
            if s[i] in '0123456789':
                result = result * 10 + int(s[i])
                i += 1
            else:
                break

        result = result * sign

        if result < -2147483648:
            return -2147483648

        if result > 2147483647:
            return 2147483647

        return result

        
        