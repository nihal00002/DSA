class Solution:
    def findFloor(self, arr, x):
        # code here
        lower_bound = -1
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low + high)//2
            if arr[mid]<= x:
                lower_bound = mid
                low = mid + 1
            else:
                high = mid - 1
        return lower_bound