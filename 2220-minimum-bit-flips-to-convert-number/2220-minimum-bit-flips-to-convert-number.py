class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        goal = start ^ goal
        count = 0
        while goal > 0:
            temp = goal%2
            if temp == 1:
                count += 1
            goal = goal//2
        return count