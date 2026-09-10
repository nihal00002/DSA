class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_num = 0
        for i in range(len(nums)+1):
            sum_num += i
        return sum_num - sum(nums)