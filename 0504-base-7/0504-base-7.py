class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        answer = []
        while num > 0:
            digit = num % 7
            answer.append(str(digit))

            num //= 7

        answer.reverse()

        result = "".join(answer)

        if negative:
            result = "-" + result

        return result
       
        