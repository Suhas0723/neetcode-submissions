class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        for i in range(0, len(nums) + 1):
            a = a ^ i
        
        b = 0
        for i in nums:
            b = b ^ i
        
        return a ^ b