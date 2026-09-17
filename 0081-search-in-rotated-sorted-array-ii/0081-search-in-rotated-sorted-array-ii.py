class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            if nums[low]<= nums[mid]:
                if nums[mid] >= target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[high]>= target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

