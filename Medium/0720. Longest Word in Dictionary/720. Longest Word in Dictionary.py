from typing import List


class Solution:
    def get_word_val(self, word: str):
        val = 0
        for i in range(len(word)):
            val += (ord(word[i]) - 97 + 1) * (26 ** i)

        return val

    def longestWord(self, words: List[str]) -> str:
        longest_word = words[0]
        max_val = self.get_word_val(longest_word)
        for i in range(1, len(words)):
            word = words[i]
            val = self.get_word_val(word)
            if val > max_val:
                max_val = val
                longest_word = word

        return longest_word


if __name__ == '__main__':
    s = Solution()

    print(s.get_word_val('apple'))
    print(s.get_word_val('aa'))
    print(s.get_word_val('apply'))
