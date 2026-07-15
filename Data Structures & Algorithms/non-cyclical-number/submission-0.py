class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def sumOfSquares(n: int):
            res = 0
            while n != 0:
                d = n % 10
                res += d**2
                n = n // 10

            return res

        while n != 1:
            oldLength = len(seen)
            seen.add(n)
            if oldLength == len(seen):
                return False 
            n = sumOfSquares(n)


        return True

            



