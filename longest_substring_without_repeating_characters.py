class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        chars = []
        for i in range(len(s)):
            if s[i] not in chars:
                chars.append(s[i])
                if i - left + 1 > max_len:
                    max_len = i - left + 1
            else:
                index = chars.index(s[i])
                left += index+1
                chars = chars[index+1:]
                chars.append(s[i])

        return max_len