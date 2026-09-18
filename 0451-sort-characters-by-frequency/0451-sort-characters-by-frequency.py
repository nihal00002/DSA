class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        char = {}
        for i in s:
            char[i] = char.get(i,0)+1
        sorted_d = dict(sorted(char.items(), key=lambda x: (-x[1],x[0])))
        for j,k in sorted_d.items():
            result += j * k
        return result