class Solution:
    def maxDepth(self, s: str) -> int:
        if len(s)==0:
            return 0
        count = 0
        maxi = 0
        for i in s:
            if i == "(":
                count += 1
                maxi = max(maxi,count)
            if i == ")":
                count -= 1
        return max(maxi,count)