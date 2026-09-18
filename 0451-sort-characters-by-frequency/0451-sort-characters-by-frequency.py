class Solution:
    def frequencySort(self, s: str) -> str:
        char = {}
        for i in s:
            char[i] = char.get(i, 0) + 1
        
        max_freq = max(char.values())
        buckets = [[] for _ in range(max_freq + 1)]
        for ch, freq in char.items():
            buckets[freq].append(ch)
        
        result = []
        for freq in range(max_freq, 0, -1):
            for ch in buckets[freq]:
                result.append(ch * freq)
        
        return "".join(result)