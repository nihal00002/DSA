class Solution:
    def countStrings(self, n):
        memo = {}
        def solve(index, flag):
            if index >= n:
                return 1
            if (index, flag) in memo:
                return memo[(index, flag)]
            count = solve(index + 1, True)
            if flag:
                count += solve(index + 1, False)
            memo[(index, flag)] = count
            return count
        return solve(0, True)