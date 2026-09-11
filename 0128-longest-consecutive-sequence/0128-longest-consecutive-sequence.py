class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        seq = 0

        while nums:
            n = nums.pop()
            current = n
            this_seq = 0
            while current - 1 in nums:
                current -= 1
                this_seq += 1
                nums.remove(current)

            current = n 
            while current + 1 in nums:
                current += 1
                this_seq += 1 
                nums.remove(current)

            seq = max(seq, this_seq + 1)
        

        return seq
