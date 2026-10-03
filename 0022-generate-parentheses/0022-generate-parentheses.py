class Solution(object):
    def generateParenthesis(self, n):
        def solve(index, brackets, total, opens, result):
            if index >= len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return
            if total < 0:
                return
            if opens < n:
                brackets[index] = "("
                solve(index + 1, brackets, total + 1, opens + 1, result)
            if total > 0:
                brackets[index] = ")"
                solve(index + 1, brackets, total - 1, opens, result)
            return result

        return solve(0, [""] * (n*2), 0, 0, [])