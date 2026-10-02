class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        def function(index,total):
            if total == k:
                return True
            if total > k:
                return False
            if index >= len(arr):
                return False
            a = total + arr[index]
            pick = function(index + 1, a)
            if pick == True:
                return True
            a = total
            not_pick = function(index + 1, a)
            return not_pick
        return function(0,0)
        