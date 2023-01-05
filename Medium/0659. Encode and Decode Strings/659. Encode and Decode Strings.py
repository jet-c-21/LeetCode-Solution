class Solution:
    def encode(self, str_ls: list) -> str:
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """

        # write your code here
        res = ''
        for s in str_ls:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, string: str) -> list:
        """
        @param: str: A string
        @return: dcodes a single string to a list of strings
        """

        # write your code here
        res = []
        i = 0
        while i < len(string):
            j = i
            while string[j] != '#':
                j += 1

            s_len = int(string[i:j])
            s = string[j + 1: j + 1 + s_len]
            res.append(s)

            i = j + 1 + s_len

        return res
