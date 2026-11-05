class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        maxi = ls = rs= 0
        r = len(cardPoints)-1

        if len(cardPoints) == k:
            return sum(cardPoints)
        for i in range(k):
            ls += cardPoints[i]
        maxi = ls
        for j in range(k-1,-1,-1):
            rs += cardPoints[r]
            ls -= cardPoints[j]
            r -= 1
            maxi = max(maxi, ls + rs)
        return maxi

