class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        ub = len(nums)
        low = 0
        high = ub - 1
        while low <= high:
            mid = (low + high)//2
            if nums[mid]>= target:
                ub = mid
                high = mid -1
            else:
                low = mid + 1
        return ub