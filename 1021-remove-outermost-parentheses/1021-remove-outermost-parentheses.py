class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        count = 0 
        for i in s:
            if i =="(":
                count += 1
                if count >1:
                    result += i
            else:
                count -= 1
                if count >0:
                    result += i
        return result