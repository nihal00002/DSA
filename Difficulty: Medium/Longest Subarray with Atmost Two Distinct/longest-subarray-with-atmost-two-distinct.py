class Solution:
    def totalElements(self, arr):
        # Code here
        my_dict = {}
        right = left = maxi = 0
        while right < len(arr):
            my_dict[arr[right]] = my_dict.get(arr[right],0) + 1
            if len(my_dict) > 2:
                my_dict[arr[left]] -= 1
                if my_dict[arr[left]] == 0:
                    del my_dict[arr[left]]
                left += 1
            if len(my_dict) <= 2:
                maxi = max(maxi, right-left+1)
            right += 1
        return maxi