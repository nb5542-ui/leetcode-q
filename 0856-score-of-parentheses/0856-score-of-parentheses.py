class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]

        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                score = stack.pop()
                stack[-1] += max(1, 2 * score)

        return stack[0]

            



        
       
        