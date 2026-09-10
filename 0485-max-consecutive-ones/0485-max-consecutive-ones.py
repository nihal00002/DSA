class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_one = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_one = max(max_one,count)
                count = 0
        return max(max_one,count)
            