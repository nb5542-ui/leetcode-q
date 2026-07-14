class Solution(object):
    def removeDuplicateLetters(self, s):

        
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        stack = []
        visited = set()

        for ch in s:

            
            freq[ch] -= 1

            
            if ch in visited:
                continue

           
            while (stack and
                   ch < stack[-1] and
                   freq[stack[-1]] > 0):

                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)