class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        temp = 0
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in store:
                return [store[temp],i]
            store[nums[i]]=i
