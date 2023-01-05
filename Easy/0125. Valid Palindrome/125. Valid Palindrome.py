class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_idx, r_idx = 0, len(s) - 1
        while l_idx < r_idx:
            while l_idx < r_idx and not self.is_alpha_num(s[l_idx]):
                l_idx += 1

            while r_idx > l_idx and not self.is_alpha_num(s[r_idx]):
                r_idx -= 1

            if s[l_idx].lower() != s[r_idx].lower():
                return False

            l_idx += 1
            r_idx -= 1

        return True

    def is_alpha_num(self, c):
        res = ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9')
        return res