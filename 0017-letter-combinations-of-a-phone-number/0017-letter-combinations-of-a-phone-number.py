class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        char_map = { "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        result = []
        def solve(index,subset):
            if index >= len(digits):
                result.append("".join(subset[:]))
                return
            for i in char_map[digits[index]]:
                subset.append(i)
                solve(index+1,subset)
                subset.pop()
            return result
        return solve(0,[])

