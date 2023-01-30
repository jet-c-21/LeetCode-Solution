class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_set = set()
        l_idx = 0
        for r_idx in range(len(s)):
            while s[r_idx] in char_set:
                char_set.remove(s[l_idx])
                l_idx += 1
            char_set.add(s[r_idx])
            res = max(res, r_idx - l_idx + 1)

        return res
