class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_freq = {}
        for i in s:
            char_freq[i] = char_freq.get(i,0)+1
        for j in t:
            if j not in char_freq:
                return False
            else:
                if char_freq[j] == 0:
                    return False
                else:
                    char_freq[j] -= 1
        return True