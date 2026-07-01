class Solution(object):
    def divide(self, dividend, divisor):

        
        if dividend == -(1 << 31) and divisor == -1:
            return (1 << 31) - 1

        
        negative = (dividend < 0) != (divisor < 0)

        
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        if negative:
            return -quotient
        return quotient
        