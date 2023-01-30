class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ''
        result = 0
        for c in s:
            # print(f"char = {c}, @ [{window.find(c)}], win = {window}")
            window = window[window.find(c) + 1:] + c
            result = max(result, len(window))
        return result


if __name__ == '__main__':
    txt = "Hello, welcome to my world."

    x = txt.find("x")
    # print(x)

    # Solution().lengthOfLongestSubstring(txt)
    # print()
    # print('Hel'[2:])