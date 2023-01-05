class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_letter_count = dict()
        t_letter_count = dict()

        for i in range(len(s)):
            s_letter_count[s[i]] = 1 + s_letter_count.get(s[i], 0)
            t_letter_count[t[i]] = 1 + t_letter_count.get(t[i], 0)

        return s_letter_count == t_letter_count
