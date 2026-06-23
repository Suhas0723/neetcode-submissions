class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            if target - i in numbers:
                print(target-i)
                return [numbers.index(i)+1, numbers.index(target - i,numbers.index(i)+1)+1]
                
        