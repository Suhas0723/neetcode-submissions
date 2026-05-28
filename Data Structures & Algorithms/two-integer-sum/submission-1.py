class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            difference = target - nums[i]
            try:
                j = nums.index(difference, i + 1)
                return [i, j]
            except:
                continue

        