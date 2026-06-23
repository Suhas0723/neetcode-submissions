class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = set()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == 0 - nums[i]:
                    output.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < 0 - nums[i]:
                    left += 1
                else: 
                    right -= 1

        output = list(output)
        print(output)
        for i in range(len(output)):
            output[i] = list(output[i])

        return output
            
                
            