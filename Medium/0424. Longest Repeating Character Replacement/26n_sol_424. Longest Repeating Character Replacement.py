class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        res = 0
        l_idx = 0
        for r_idx in range(len(s)):
            char_count[s[r_idx]] = 1 + char_count.get(s[r_idx], 0)

            while (r_idx - l_idx + 1) - max(char_count.values()) > k:
                char_count[s[l_idx]] -= 1
                l_idx += 1

            res = max(res, r_idx - l_idx + 1)

        return res
