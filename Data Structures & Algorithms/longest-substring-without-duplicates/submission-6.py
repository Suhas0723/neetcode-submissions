from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        left = right = 0
        longest = 1
        chars = defaultdict(int)

        while right < len(s):
            if s[right] not in chars:
                chars[s[right]] += 1
                if ((right - left) + 1) > longest:
                    longest = (right - left) + 1
                right += 1
            else:
                chars.clear()
                left += 1
                right = left
        return longest
                


