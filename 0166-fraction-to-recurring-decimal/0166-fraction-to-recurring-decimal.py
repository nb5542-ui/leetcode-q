class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        ans = ""
        if (numerator < 0) != (denominator < 0):
            ans += "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        ans += str(numerator // denominator)

        remainder = numerator % denominator

        if remainder == 0:
            return ans

        ans += "."
        seen = {}

        while remainder != 0:
            if remainder in seen:
                pos = seen[remainder]
                ans = ans[:pos] + "(" + ans[pos:] + ")"
                return ans

            seen[remainder] = len(ans)

            remainder *= 10

            digit = remainder // denominator
            ans += str(digit)

            remainder %= denominator

        return ans 
        
        