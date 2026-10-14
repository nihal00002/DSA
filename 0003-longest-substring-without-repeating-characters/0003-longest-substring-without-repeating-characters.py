class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi = 0
        dict = {}
        low = high = 0
        while high < len(s):
            if s[high] in dict:
                low = max(low,dict[s[high]]+1)
            maxi = max(maxi, high - low + 1)
            dict[s[high]] = high
            high += 1
        return maxi
        