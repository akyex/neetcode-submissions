class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            leftover = target - num
            if leftover in seen:
                return [seen[leftover], index]
            seen[num] = index
        return []
        