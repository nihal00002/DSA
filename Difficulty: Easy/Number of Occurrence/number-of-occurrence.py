class Solution:
    def countFreq(self, arr, target):
        # code here
        def lower_bound(arr):
            low = 0
            high = len(arr)-1
            lb = -1
            while low <= high:
                mid = (low + high)//2
                if arr[mid] >= target:
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return lb
        def upper_bound(arr):
            low = 0
            high = len(arr) - 1
            ub = len(arr)
            while low <= high:
                mid = (low + high)//2
                if arr[mid]> target:
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1 
            return ub
        lower = lower_bound(arr)
        if lower == -1:
            return 0

        upper = upper_bound(arr)
        
        
        return upper - lower