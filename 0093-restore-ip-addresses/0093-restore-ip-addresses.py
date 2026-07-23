class Solution(object):
    def restoreIpAddresses(self, s):
        ans = []
        path = []
        def dfs(index):
            if len(path) == 4:
                if index == len(s):
                    ans.append(".".join(path))

                return

            for length in range(1,4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                if len(part) > 1 and part[0] == '0':
                    continue
                if int(part) > 255:
                    continue

                path.append(part)

                dfs(index + length)

                path.pop()

        dfs(0)
        return ans
        
        