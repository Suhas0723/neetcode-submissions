class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        self.helper(0, [], combs, nums, target)
        return combs

    def helper(self, i, curComb, combs, nums, target):

        if target == 0:
            combs.append(curComb.copy())
            return
        if target < 0 or i >= len(nums):
            return

        for j in range(i, len(nums)):
            curComb.append(nums[j])
            self.helper(j, curComb, combs, nums, target - nums[j])
            curComb.pop()

        