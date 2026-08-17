class Solution(object):
    def compress(self, chars):

        read = 0
        write = 0

        while read < len(chars):

            
            j = read

            while j < len(chars) and chars[j] == chars[read]:
                j += 1

           
            count = j - read

            
            chars[write] = chars[read]
            write += 1

            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            
            read = j

        return write
                



        
        
        
        


        
        