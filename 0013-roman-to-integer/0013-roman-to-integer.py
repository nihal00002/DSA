class Solution:
    def romanToInt(self, s: str) -> int:
        latter = {"I":1,"V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}
        result = 0
        for i in range(len(s)-1):
            if latter[s[i]] < latter[s[i+1]]:
                result -= latter[s[i]]
            else:
                result += latter[s[i]]
        result += latter[s[-1]]
        return result 
            


            
