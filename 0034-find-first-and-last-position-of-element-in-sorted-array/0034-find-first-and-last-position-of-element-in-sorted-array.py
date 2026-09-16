class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower_bound(nums):
            low = 0
            high = len(nums) -1 
            lower_bound = -1 
            while low <= high:
                mid = (low + high)//2
                if nums[mid] >= target:
                    lower_bound = mid 
                    high = mid - 1
                else: 
                    low = mid + 1
            return lower_bound
        def upper_bound(nums):
            low = 0
            high = len(nums) -1 
            upper_bound = len(nums)
            while low <= high:
                mid = (low + high)//2
                if nums[mid] > target:
                    upper_bound = mid 
                    high = mid - 1
                else: 
                    low = mid + 1
            return upper_bound

        lower = lower_bound(nums)
        upper = upper_bound(nums)

        if lower == -1 or lower == len(nums) or nums[lower] != target:
            return [-1, -1]
        return [lower, upper - 1]
        
       