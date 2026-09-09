class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        curr_count = 0
        for index in range(len(nums)):
            if nums[index] == 1:
                curr_count += 1
                output = max(output, curr_count)
            else:
                curr_count = 0
        return output