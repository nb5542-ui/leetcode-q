class Solution(object):
    def reverseStr(self, s, k):
        count = 0
        s = list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k] = reversed(s[i:i+k])

        return "".join(s)


            
            

       

            

        

        
        