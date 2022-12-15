# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2022/12/15
"""
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''
        valid_char = list(string.ascii_letters) + list(string.digits)
        for char in s:
            if char in valid_char:
                clean_str += char

        clean_str = clean_str.lower()

        for i in range(len(clean_str)):
            forward_char = clean_str[i]
            backward_char = clean_str[len(clean_str) - 1 - i]
            if forward_char != backward_char:
                return False

        return True


if __name__ == '__main__':
    a = "0P"
    Solution().isPalindrome(a)
