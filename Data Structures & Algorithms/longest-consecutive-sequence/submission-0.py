class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            if (i-1) not in nums:
                length = 0
                while (i + length) in nums:
                    length += 1
                
                if length > longest:
                    longest = length
        
        return longest
