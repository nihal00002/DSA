class Solution:
    def findMin(self, n: int) -> int:
        coins = [1,2,5,10]
        j = len(coins) - 1
        count = 0
        while j>= 0 and n >= 0:
            if n >= coins[j]:
                count += 1
                n -= coins[j]
            else:
                j -= 1
        return count
                