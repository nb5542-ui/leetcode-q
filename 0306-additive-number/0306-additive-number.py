class Solution(object):
    def isAdditiveNumber(self, num):

        def dfs(index, prev, curr, count):

            # Base Case
            if index == len(num):
                return count >= 3

            for end in range(index, len(num)):

                part = num[index:end + 1]

                # Leading zero check
                if len(part) > 1 and part[0] == '0':
                    break

                value = int(part)

                # First two numbers
                if count < 2:
                    if dfs(end + 1, curr, value, count + 1):
                        return True

                else:

                    expected = prev + curr

                    if value < expected:
                        continue

                    elif value > expected:
                        break

                    else:
                        if dfs(end + 1, curr, value, count + 1):
                            return True

            return False

        return dfs(0, 0, 0, 0)



        
        