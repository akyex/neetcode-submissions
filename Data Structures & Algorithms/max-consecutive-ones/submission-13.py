class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_output = 0
        curr_ones = 0
        for index in range(len(nums)):
            if nums[index] == 1:
                curr_ones += 1 
                max_output = max(max_output, curr_ones)
            else:
                curr_ones = 0
        return max_output