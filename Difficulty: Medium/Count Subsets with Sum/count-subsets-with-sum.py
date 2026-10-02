class Solution:
    def perfectSum(self, arr, target):
        memo = {}
        def function(index, total):
            if index >= len(arr):
                return 1 if target == total else 0
            if (index, total) in memo:
                return memo[(index, total)]
            sum_ = total + arr[index]
            pick = function(index + 1, sum_)
            not_pick = function(index + 1, total)
            memo[(index, total)] = pick + not_pick
            return memo[(index, total)]
        return function(0, 0)