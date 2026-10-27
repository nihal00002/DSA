class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zero = maxi = high = low = 0
        while high < len(nums):
            if nums[high] == 0:
                zero += 1
            if zero > k:
                while zero > k:
                    if nums[low] == 0:
                        zero -= 1
                    low += 1
            maxi = max(maxi,high-low+1)
            high += 1

        return maxi


        