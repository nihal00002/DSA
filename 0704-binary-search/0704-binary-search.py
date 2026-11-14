class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums)-1
        low = 0
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1 
            else:
                low = mid + 1
        return -1
            