class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        longest = 0
        visited = set()
        for i in s:
            while i in visited:
                visited.remove(s[left])
                left += 1
            
            visited.add(i)
            right += 1
            longest = max(longest, (right - left))
            
        
        return longest
