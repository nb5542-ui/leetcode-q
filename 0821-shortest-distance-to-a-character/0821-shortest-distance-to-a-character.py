class Solution(object):
    def shortestToChar(self, s, c):

        result = []

        for i in range(len(s)):

            min_dis = float('inf')

            for j in range(len(s)):

                if s[j] == c:
                    min_dis = min(min_dis, abs(i - j))

            result.append(min_dis)

        return result
        
        
       
        
                


        





        