class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if -nums[i] == (nums[left] + nums[right]):
                    triples.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif -nums[i] < (nums[left] + nums[right]):
                    right -= 1
                else: 
                    left += 1

        output = []
        for i in triples:
            output.append(list(i))

        return output


